#!/usr/bin/env python3
"""Render a blog post from blog-routine/posts/<slug>.json into public/blog-<slug>.html,
then refresh the blog index cards and the sitemap.

Usage:  python3 blog-routine/build_post.py <slug>        (one post)
        python3 blog-routine/build_post.py --all         (rebuild every post + index)

Exits non-zero when the post breaks a rule from blog-routine/seo (title/description length,
banned filler, em dashes, missing sections, broken internal links, unlinked sources).
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
POSTS = ROOT / "blog-routine" / "posts"
SITE = "https://shahmikh.com"
PERSON_ID = SITE + "/about.html#person"

BANNED = [
    r"in today'?s fast[- ]paced", r"in the digital age", r"\bunlock", r"\bunleash", r"\belevate",
    r"game[- ]changer", r"\bdive in", r"navigate the landscape", r"it'?s important to note",
    r"in conclusion", r"whether you'?re", r"look no further", r"\bseamless", r"\brobust",
    r"\bleverag", r"supercharge",
]

HEADER = """<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container nav-row">
    <a href="index.html" class="brand"><span class="brand-mark" aria-hidden="true">S</span>Shahmikh</a>
    <nav class="nav-links" id="nav-links" aria-label="Primary">
      <a href="courses.html">Subjects</a><a href="index.html#how">How it works</a><a href="pricing.html">Pricing</a><a href="testimonials.html">Reviews</a><a href="blog.html" class="is-active">Blog</a><a href="about.html">About</a>
    </nav>
    <div class="nav-cta">
      <a href="contact.html" class="btn btn--ghost">Contact</a>
      <a href="contact.html#booking" class="btn btn--primary">Book a free call</a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="Toggle menu"><span></span></button>
    </div>
  </div>
</header>
"""

FOOTER = """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col"><h4>Syed Shahmikh Ali</h4><p>Engineer turned educator — helping students, parents and career-changers with exam strategy, degree and career decisions, and tech skills.</p></div>
      <div class="footer-col"><h4>Explore</h4><ul><li><a href="about.html">About</a></li><li><a href="courses.html">Courses</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="blog.html">Blog</a></li></ul></div>
      <div class="footer-col"><h4>Programs</h4><ul><li><a href="courses.html">Security+ &amp; CCNA</a></li><li><a href="courses.html">AP CSP, CSA &amp; IB CS</a></li><li><a href="career-guidance.html">Career Guidance</a></li></ul></div>
      <div class="footer-col"><h4>Connect</h4><ul><li><a href="contact.html">Contact</a></li><li><a href="faq.html">FAQ</a></li><li><a href="testimonials.html">Testimonials</a></li><li><a class="social-link" href="#" data-network="youtube" rel="noopener" target="_blank">YouTube</a></li><li><a class="social-link" href="#" data-network="instagram" rel="noopener" target="_blank">Instagram</a></li></ul></div>
    </div>
    <div class="footer-bottom"><span>© 2026 Syed Shahmikh Ali. All rights reserved.</span><span>Teaching students across the US, UK &amp; Europe.</span></div>
  </div>
</footer>
<script src="main.js"></script>
"""

AUTHOR_BOX = """<aside class="author-box">
  <img src="headshot.jpg" alt="Syed Shahmikh Ali" width="72" height="72" loading="lazy">
  <div>
    <p class="author-name">About the author</p>
    <p><a href="about.html">Syed Shahmikh Ali</a> is a Preply Super Tutor, in the top 15% of computer science tutors on Preply, with a mechatronics engineering background. He teaches AP CSP, AP CSA, IB CS, IGCSE CS, Python, Java, Security+ and CCNA one to one.</p>
    <p class="post-note">Editorial note: this article is written with AI assistance and checked against the sources listed above. If you spot a mistake, tell me through the <a href="contact.html">contact page</a> and I will correct it.</p>
  </div>
</aside>"""


def esc(s):
    return html.escape(s, quote=True)


def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def load(slug):
    return json.loads((POSTS / (slug + ".json")).read_text(encoding="utf-8"))


def all_slugs():
    return sorted(p.stem for p in POSTS.glob("*.json"))


def validate(p):
    errs, warns = [], []
    slug = p["slug"]
    if len(p["title"]) > 60:
        errs.append("title is %d chars (max 60)" % len(p["title"]))
    if not 140 <= len(p["description"]) <= 160:
        errs.append("description is %d chars (need 140-160)" % len(p["description"]))
    if not 3 <= len(p["takeaways"]) <= 5:
        errs.append("need 3-5 takeaways")
    if len(p["sections"]) < 4:
        errs.append("need at least 4 sections")
    if len(p["faq"]) != 3:
        errs.append("need exactly 3 FAQ items")
    if not 2 <= len(p["sources"]) <= 6:
        errs.append("need 2-6 sources")
    if len(p["related"]) < 2:
        errs.append("need at least 2 related links")
    body = " ".join([p["lead"]] + p["takeaways"] + [s["h2"] + " " + s["html"] for s in p["sections"]]
                    + [f["q"] + " " + f["a"] for f in p["faq"]])
    text = plain(body)
    for pat in BANNED:
        m = re.search(pat, text, re.I)
        if m:
            errs.append("banned filler phrase: %r" % m.group(0))
    if "—" in text or "–" in text:
        errs.append("dash characters found in body; use commas or periods")
    words = len(text.split())
    if words < 700:
        warns.append("only %d words" % words)
    if words > 2400:
        warns.append("%d words is long; check for padding" % words)
    for s in p["sources"]:
        if not s["url"].startswith("https://"):
            errs.append("source is not https: " + s["url"])
        if s["url"] not in body:
            errs.append("source not linked inline in the article: " + s["url"])
    for m in re.finditer(r'href="([^"]+)"', body):
        h = m.group(1)
        if h.startswith("http") or h.startswith("#") or h.startswith("mailto:"):
            continue
        f = h.split("#")[0]
        if not (PUB / f).exists() and not (POSTS / (f.replace("blog-", "").replace(".html", "") + ".json")).exists():
            errs.append("internal link target missing: " + h)
    for r in p["related"]:
        f = r["href"].split("#")[0]
        if not (PUB / f).exists() and not (POSTS / (f.replace("blog-", "").replace(".html", "") + ".json")).exists():
            errs.append("related link target missing: " + r["href"])
    ids = [s["id"] for s in p["sections"]]
    if len(ids) != len(set(ids)):
        errs.append("duplicate section ids")
    return errs, warns, words


def render(p):
    slug = p["slug"]
    url = "%s/blog-%s.html" % (SITE, slug)
    tocs = "".join('<li><a href="#%s">%s</a></li>' % (s["id"], esc(s["h2"])) for s in p["sections"])
    tocs += '<li><a href="#faq">Frequently asked questions</a></li><li><a href="#sources">Sources</a></li>'
    sections = "".join('\n      <h2 id="%s">%s</h2>\n      %s\n' % (s["id"], esc(s["h2"]), s["html"]) for s in p["sections"])
    faq = "".join(
        '\n        <details class="faq-item"><summary>%s <span class="icon" aria-hidden="true"></span></summary><p>%s</p></details>'
        % (esc(f["q"]), f["a"]) for f in p["faq"])
    sources = "".join('<li><a href="%s" rel="noopener">%s</a></li>' % (esc(s["url"]), esc(s["title"])) for s in p["sources"])
    related = "".join('<li><a href="%s">%s</a></li>' % (esc(r["href"]), esc(r["title"])) for r in p["related"])
    takeaways = "".join("<li>%s</li>" % t for t in p["takeaways"])

    graph = [
        {
            "@type": "Person", "@id": PERSON_ID, "name": "Syed Shahmikh Ali", "url": SITE + "/about.html",
            "image": SITE + "/headshot.jpg", "jobTitle": "Tutor and career mentor",
            "knowsAbout": ["AP Computer Science A", "AP Computer Science Principles", "IB Computer Science",
                           "Java", "Python", "CompTIA Security+", "Cisco CCNA"],
        },
        {
            "@type": "BlogPosting", "headline": p["title"], "description": p["description"],
            "image": [SITE + "/headshot.jpg"], "datePublished": p["published"], "dateModified": p["modified"],
            "author": {"@id": PERSON_ID}, "publisher": {"@id": PERSON_ID}, "inLanguage": "en",
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "citation": [s["url"] for s in p["sources"]],
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog.html"},
                {"@type": "ListItem", "position": 3, "name": p["title"], "item": url},
            ],
        },
        {
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": f["q"],
                            "acceptedAnswer": {"@type": "Answer", "text": plain(f["a"])}} for f in p["faq"]],
        },
    ]
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)

    cta_eyebrow = p.get("cta_eyebrow", "Want help with this?")
    cta_heading = p.get("cta_heading", "Book a short call and we will make a plan")

    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B1B33">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}/headshot.jpg">
<meta property="article:published_time" content="{pub}">
<meta property="article:modified_time" content="{mod}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/headshot.jpg">
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="pages.css">
<link rel="stylesheet" href="theme.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{header}
<main id="main">
  <section class="page-hero">
    <div class="container">
      <p class="eyebrow">{eyebrow} · {mins} min read</p>
      <h1 style="max-width: 24ch;">{h1}</h1>
      <p class="post-byline">By <a href="about.html">Syed Shahmikh Ali</a> · Published {pub} · Updated {mod}</p>
    </div>
  </section>

  <article class="section-tight">
    <div class="container blog-post-body">
      <p class="post-lead">{lead}</p>

      <div class="takeaways">
        <h2>Key takeaways</h2>
        <ul>{takeaways}</ul>
      </div>

      <nav class="toc" aria-label="Contents"><p class="toc-title">In this article</p><ol>{toc}</ol></nav>
{sections}
      <h2 id="faq">Frequently asked questions</h2>
      <div class="faq-list">{faq}
      </div>

      <h2 id="sources">Sources</h2>
      <ul class="post-sources">{sources}</ul>

      <h2>Related reading</h2>
      <ul class="post-sources">{related}</ul>

      {author}
    </div>
  </article>

  <section class="on-ink cta-band">
    <div class="container">
      <p class="eyebrow">{cta_eyebrow}</p>
      <h2>{cta_heading}</h2>
      <a href="contact.html#booking" class="btn btn--gold">Book a Call</a>
    </div>
  </section>
</main>

{footer}</body>
</html>
""".format(title=esc(p["title"]), desc=esc(p["description"]), url=url, site=SITE, pub=p["published"],
           mod=p["modified"], ld=ld, header=HEADER, eyebrow=esc(p["eyebrow"]), mins=p["read_min"],
           h1=esc(p["h1"]), lead=p["lead"], takeaways=takeaways, toc=tocs, sections=sections, faq=faq,
           sources=sources, related=related, author=AUTHOR_BOX, cta_eyebrow=esc(cta_eyebrow),
           cta_heading=esc(cta_heading), footer=FOOTER)


def update_index():
    slugs = all_slugs()
    posts = sorted((load(s) for s in slugs), key=lambda x: (x["published"], x["slug"]), reverse=True)
    cards = "".join(
        """
        <a href="blog-{slug}.html" class="card blog-card reveal">
          <span class="eyebrow">{eyebrow}</span>
          <h3>{title}</h3>
          <p>{summary}</p>
          <div class="blog-meta"><span>{mins} min read</span></div>
        </a>""".format(slug=p["slug"], eyebrow=esc(p["eyebrow"]), title=esc(p["h1"]),
                       summary=esc(p["card_summary"]), mins=p["read_min"]) for p in posts)
    f = PUB / "blog.html"
    s = f.read_text(encoding="utf-8")
    block = "<!-- POSTS:START -->" + cards + "\n        <!-- POSTS:END -->"
    if "<!-- POSTS:START -->" in s:
        s = re.sub(r"<!-- POSTS:START -->.*?<!-- POSTS:END -->", lambda m: block, s, flags=re.S)
    else:
        s = s.replace('<div class="blog-grid">', '<div class="blog-grid">\n        ' + block, 1)
    f.write_text(s, encoding="utf-8")
    newest = max((p["modified"] for p in posts), default=None)
    return newest


def update_sitemap(posts_meta, index_date):
    f = PUB / "sitemap.xml"
    s = f.read_text(encoding="utf-8")

    def put(loc, date):
        nonlocal s
        entry = "  <url><loc>%s</loc><lastmod>%s</lastmod></url>" % (loc, date)
        pat = re.compile(r"  <url><loc>%s</loc>(?:<lastmod>[^<]*</lastmod>)?</url>" % re.escape(loc))
        if pat.search(s):
            s = pat.sub(lambda m: entry, s)
        else:
            s = s.replace("</urlset>", entry + "\n</urlset>")

    for slug, date in posts_meta:
        put("%s/blog-%s.html" % (SITE, slug), date)
    if index_date:
        put(SITE + "/blog.html", index_date)
    f.write_text(s, encoding="utf-8")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    slugs = all_slugs() if args[0] == "--all" else args
    failed = False
    meta = []
    for slug in slugs:
        p = load(slug)
        errs, warns, words = validate(p)
        for w in warns:
            print("[warn] %s: %s" % (slug, w))
        if errs:
            failed = True
            for e in errs:
                print("[ERROR] %s: %s" % (slug, e))
            continue
        (PUB / ("blog-%s.html" % slug)).write_text(render(p), encoding="utf-8")
        meta.append((slug, p["modified"]))
        print("[ok] %s: %d words, public/blog-%s.html written" % (slug, words, slug))
    if failed:
        sys.exit(1)
    newest = update_index()
    update_sitemap(meta, newest)
    print("[ok] blog.html cards and sitemap.xml updated")


if __name__ == "__main__":
    main()
