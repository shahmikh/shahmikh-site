# Blog routine for shahmikh.com

Run by the scheduled task (Monday and Thursday, 08:44 Asia/Karachi). One run = one new post.
The owner asked for two posts a week, written with the SEO skill in `blog-routine/seo/`. Follow it every time.

## Steps

1. **Get the repo.** Attach `shahmikh/shahmikh-site` with push access, clone it (or `git pull --ff-only origin main` if it already exists).
2. **Read the rules.** Read `blog-routine/seo/SKILL.md`, `references/content-playbook.md` and `references/technical-schema.md`. Read `blog-routine/topics.md` for the backlog and the published log.
3. **Pick the topic.** Take the first unused topic in the backlog. Check it does not overlap an existing post in `public/` (cannibalisation). If it does, pick the next one. If fewer than 4 topics are left, add 6 new ones to the backlog first, aimed at the owner's audience (parents and students of AP CSP, AP CSA, IB CS, IGCSE CS, Security+, CCNA, Python, Java, plus study strategy and career guidance).
4. **Research with real sources.** Use WebSearch and WebFetch. Prefer official sources (College Board, Cambridge, IB, CompTIA, Cisco, government, platform docs). Use only URLs you actually fetched this run and confirmed exist. Check every number, date and exam format against the page. If you cannot verify a fact, leave it out.
5. **Find a non-commodity angle.** Each post needs one thing a generic article lacks: a decision framework, a worked example, a tested practice routine, a clear opinion with the reason. Label hypothetical examples as examples.
6. **Write the post** as `blog-routine/posts/<slug>.json`. Copy the shape of an existing file in that folder. Rules:
   - Title at most 60 characters. Meta description 140 to 160 characters.
   - Lead answers the question in the first 2 sentences. 3 to 5 key takeaways. Question-style H2s that open with a direct answer. Exactly 3 FAQ items. 2 to 6 sources, each also linked inline in the body.
   - Aim for 900 to 1,800 words. Never pad.
   - No invented statistics, studies, clients, quotes, student stories or results. First person only for things that are plainly true of teaching (for example "I teach both courses"), never for made-up anecdotes.
   - Do not repeat or strengthen these unverified site claims: "AWS Cloud Engineer", "97 reviews", "4,500+ hours", "9 tracks", or any prices. The Preply facts (Super Tutor, top 15% of computer science tutors) are confirmed.
   - Plain, casual, specific voice. No filler phrases from the playbook's banned list, no em dashes or en dashes, no triplets of adjectives.
   - Link to a relevant service page (`courses.html`, `career-guidance.html` or `contact.html#booking`) and 1 to 2 related posts. Add one sentence with a link to the new post in one older relevant post.
7. **Build.** `python3 blog-routine/build_post.py <slug>`. Fix every `[ERROR]` and rerun until it passes. The script writes `public/blog-<slug>.html`, refreshes the cards on `public/blog.html` and updates `public/sitemap.xml`.
8. **Check.** Run `NODE_PATH=$(npm root -g) node blog-routine/seo/scripts/site_check.js public https://shahmikh.com`. The new page must have no issues (older pages may still list meta length issues, ignore those). Also confirm no horizontal scroll at 390px.
9. **Publish.** Update `blog-routine/topics.md` (move the topic to the published log with date and slug). Commit with a clear message, `git fetch origin main`, rebase if needed, push to `main`. Cloudflare redeploys in about a minute.
10. **IndexNow (best effort).** `curl -s -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json' -d '{"host":"shahmikh.com","key":"<contents of blog-routine/indexnow.key>","keyLocation":"https://shahmikh.com/<key>.txt","urlList":["https://shahmikh.com/blog-<slug>.html"]}'`. If the network blocks it, skip and carry on.
11. **Report.** Send the owner a short message (SendUserMessage) with the post title, its URL (`https://shahmikh.com/blog-<slug>.html`) and anything that needs their attention.

## Guardrails

- If validation fails after 3 honest attempts, a key fact cannot be verified, or the push fails: do NOT publish. Write what happened in `blog-routine/topics.md` under "Skipped" and tell the owner.
- Never edit `wrangler.jsonc`. The site is served from `public/`.
- Do not change existing posts beyond adding one internal link.
- Quality over volume. If a topic has no real angle, swap it for a better one.
