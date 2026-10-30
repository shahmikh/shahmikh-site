# Weekly Pinterest routine (shahmikh.com)

Goal: each week create 3 new pins from the newest blog posts / free guide and SCHEDULE them with Pinterest's native scheduler (Publish at a later date). No fake scrolling, liking or following. Needs the user's Chrome with Pinterest signed in (account @shahmikhali).

1. `git pull` the repo (shahmikh/shahmikh-site). Read `blog-routine/posts/` and `public/blog-*.html` to find posts not yet pinned (see `pinterest-routine/pinned.md`, the log of pinned slugs).
2. Pick 3 posts. Take text ONLY from the post's verified takeaways/numbers. Never invent claims, stats or guarantees.
3. Add entries to `mk.py` (f, kicker, title, 4 items), then in a working dir copy mk.py, t.html, shot.js and run `python3 mk.py && node shot.js` to produce 1000x1500 PNGs (needs Playwright; fonts are in public/fonts).
4. In Chrome open https://www.pinterest.com/pin-builder/ . Upload PNG with file_upload (ref of "File upload" button). Set title (<=100 chars, keyword first) and link via form_input, e.g. `https://shahmikh.com/<slug>?utm_source=pinterest&utm_medium=social&utm_campaign=pins` (extensionless URL). Description: click the box and type 2-3 plain sentences + 4-5 hashtags, ~300-500 chars, mention shahmikh.com.
5. Board: open dropdown (866,184) -> pick the matching board (AP CS & IB Computer Science Tips; Study & Productivity for Tech Students; Cybersecurity Career Roadmap; Cloud & DevSecOps Career Paths; AI Explained; Raising a Future Tech Kid). Do board BEFORE typing the description (the page scrolls).
6. Scroll down, choose "Publish at a later date", open calendar icon, pick the date, keep 12:00. Space pins 2 days apart starting the day after the last scheduled pin (check pinterest.com/shahmikhali/_created/ "Scheduled Pins"). Click Publish (top, after scrolling up); confirm "Pin Scheduled".
7. Append the slugs and dates to `pinterest-routine/pinned.md`, commit and push.
8. Report: what was scheduled, dates, and any Pinterest analytics visible (impressions/clicks) plus Pinterest visits from Cloudflare Web Analytics referrers if reachable.
