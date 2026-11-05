# Weekly Pinterest routine (shahmikh.com)

Goal: each week create 3 new pins from the newest blog posts / free guide and SCHEDULE them with Pinterest's native scheduler (Publish at a later date). No fake scrolling, liking or following. Needs the user's Chrome with Pinterest signed in (account @shahmikhali).

1. `git pull` the repo (shahmikh/shahmikh-site). Read `blog-routine/posts/` and `public/blog-*.html` to find posts not yet pinned (see `pinterest-routine/pinned.md`, the log of pinned slugs).
2. Pick 3 posts. Take text ONLY from the post's verified takeaways/numbers. Never invent claims, stats or guarantees.
3. Add entries to `mk.py` (f, kicker, title, 4 items), then in a working dir copy mk.py, t.html, shot.js and run `python3 mk.py && node shot.js` to produce 1000x1500 PNGs (needs Playwright; fonts are in public/fonts).
3b. What the research says works (checked 5 Nov 2026; sources: Tailwind 2025 benchmark of ~1.2M pins, GenSumo 2026 benchmark of 148k pins; both are tool vendors, so treat as directional):
   - Static vertical image pins (2:3, 1000x1500) are about 89% of the most viral pins and give the most outbound clicks per impression. Keep making them. Video gets reach and saves but few clicks.
   - Carousels get close to static for clicks with more saves. Make one carousel pin per week for step-by-step or plan content (study plan, weekly schedule) when the pin builder offers it.
   - Always add alt text (describe the pin in one plain sentence with the topic keywords). Tailwind reports pins with alt text get far more outbound clicks, though its text and chart figures disagree, so the size of the effect is uncertain.
   - A few pins drive most results (top 1% = over half of impressions and clicks), so make several different designs for the same page over time (new pin, same URL) instead of one pin per post. Re-pin the best post with a new headline and layout a few weeks later.
   - Text overlay vs no text is not settled by any data found. Keep the clear headline, but vary layouts (list, checklist, question, before/after).
   - Keyword-first titles and descriptions (what a parent or student would search), Pinterest search drives discovery.
   - Do not judge results before 3 to 4 weeks. The account is new (39 impressions in the first 30 days).
4. In Chrome open https://www.pinterest.com/pin-builder/ . Upload PNG with file_upload (ref of "File upload" button). Set title (<=100 chars, keyword first) and link via form_input, e.g. `https://shahmikh.com/<slug>?utm_source=pinterest&utm_medium=social&utm_campaign=pins` (extensionless URL). Alt text: click "Add alt text" and type one plain sentence describing the pin with the main keyword. Description: click the box and type 2-3 plain sentences + 4-5 hashtags, ~300-500 chars, mention shahmikh.com.
5. Board: open dropdown (866,184) -> pick the matching board (AP CS & IB Computer Science Tips; Study & Productivity for Tech Students; Cybersecurity Career Roadmap; Cloud & DevSecOps Career Paths; AI Explained; Raising a Future Tech Kid). Do board BEFORE typing the description (the page scrolls).
6. Scroll down, choose "Publish at a later date", open calendar icon, pick the date, keep 12:00. Space pins 2 days apart starting the day after the last scheduled pin (check pinterest.com/shahmikhali/_created/ "Scheduled Pins"). Click Publish (top, after scrolling up); confirm "Pin Scheduled".
7. Append the slugs and dates to `pinterest-routine/pinned.md`, commit and push.
8. Report: what was scheduled, dates, and any Pinterest analytics visible (impressions/clicks) plus Pinterest visits from Cloudflare Web Analytics referrers if reachable.
