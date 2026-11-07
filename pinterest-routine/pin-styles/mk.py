import json
F='file:///home/claude/shahmikh-site/public/fonts/'
H='''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:J;font-weight:700;src:url(%splus-jakarta-sans-latin-700-normal.woff2)}
@font-face{font-family:J;font-weight:800;src:url(%splus-jakarta-sans-latin-800-normal.woff2)}
*{box-sizing:border-box;margin:0}
body{width:1000px;height:1500px;font-family:J,sans-serif;position:relative;overflow:hidden}
.foot{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-weight:800;font-size:34px}
%s</style></head><body>%s</body></html>'''
pins={}
# 1 Security+ big number (dark)
pins['sp-bignum']=('''body{background:#0A1628;color:#fff}
.k{position:absolute;top:80px;left:64px;font-weight:800;font-size:34px;letter-spacing:.1em;text-transform:uppercase;color:#19D3F3}
.n{position:absolute;top:150px;left:0;right:0;text-align:center;font-weight:800;font-size:520px;line-height:1;letter-spacing:-.04em;color:#19D3F3}
.n small{font-size:240px}
.cap{position:absolute;top:720px;left:64px;right:64px;text-align:center;font-weight:800;font-size:76px;line-height:1.1}
.cap em{font-style:normal;color:#19D3F3}
.box{position:absolute;left:64px;right:64px;top:1000px;display:flex;gap:24px}
.box div{flex:1;border:4px solid #19D3F3;border-radius:28px;padding:28px;font-weight:700;font-size:34px;line-height:1.25}
.box b{display:block;font-size:64px;color:#19D3F3;font-weight:800}
.foot{color:#fff}.foot span:last-child{color:#19D3F3}''',
'''<div class="k">CompTIA Security+ SY0-701</div><div class="n">28<small>%</small></div>
<div class="cap">of the exam is <em>Security Operations</em>. Study it first.</div>
<div class="box"><div><b>22%</b>Threats, Vulnerabilities and Mitigations</div><div><b>90</b>questions in 90 minutes, pass at 750 of 900</div></div>
<div class="foot"><span>Syed Shahmikh Ali</span><span>shahmikh.com</span></div>''')
# 2 CCNA bars (light navy on paper)
pins['ccna-bars']=('''body{background:#F4F1EA;color:#10243E}
.k{position:absolute;top:80px;left:64px;background:#10243E;color:#F4F1EA;font-weight:800;font-size:30px;padding:12px 26px;border-radius:12px}
h1{position:absolute;top:170px;left:64px;right:64px;font-weight:800;font-size:96px;line-height:1.02;letter-spacing:-.02em}
h1 em{font-style:normal;background:#FFD23F;padding:0 14px}
.bars{position:absolute;top:560px;left:64px;right:64px}
.b{margin-bottom:54px}.b p{font-weight:800;font-size:40px;margin-bottom:14px;display:flex;justify-content:space-between}
.b i{display:block;height:74px;border-radius:14px;background:#10243E}
.note{position:absolute;left:64px;right:64px;top:1180px;background:#FFD23F;border-radius:24px;padding:30px 34px;font-weight:800;font-size:38px;line-height:1.2}
.foot{color:#10243E}''',
'''<div class="k">CISCO CCNA 200-301</div><h1>What is <em>actually</em> on the exam</h1>
<div class="bars"><div class="b"><p><span>IP Connectivity</span><span>25%</span></p><i style="width:100%"></i></div>
<div class="b"><p><span>Network Fundamentals</span><span>20%</span></p><i style="width:80%"></i></div>
<div class="b"><p><span>Network Access</span><span>20%</span></p><i style="width:80%"></i></div></div>
<div class="note">Last day to take v1.1: 2 Feb 2027, per Cisco</div>
<div class="foot"><span>Syed Shahmikh Ali</span><span>shahmikh.com</span></div>''')
# 3 Python vs Java split (mint / dark)
pins['py-java-split']=('''body{background:#0F2F2A;color:#fff}
.top{position:absolute;top:0;left:0;right:0;height:520px;background:#DDF3E8;color:#0F2F2A;padding:80px 64px}
.top span{font-weight:800;font-size:30px;letter-spacing:.1em;color:#0E8F6B}
.top h1{font-weight:800;font-size:110px;line-height:1;margin-top:20px;letter-spacing:-.02em}
.half{position:absolute;top:520px;bottom:0;width:500px;padding:60px 44px}
.l{left:0;background:#0E8F6B}.r{right:0;background:#0F2F2A}
.half h2{font-weight:800;font-size:90px;margin-bottom:26px}
.half p{font-weight:700;font-size:38px;line-height:1.3;margin-bottom:26px}
.vs{position:absolute;left:440px;top:480px;width:120px;height:120px;border-radius:50%;background:#FFD23F;color:#0F2F2A;font-weight:800;font-size:46px;display:flex;align-items:center;justify-content:center;z-index:3}
.win{position:absolute;left:64px;right:64px;bottom:120px;background:#FFD23F;color:#0F2F2A;border-radius:24px;padding:26px 30px;font-weight:800;font-size:38px;text-align:center;z-index:4}
.foot{z-index:5;color:#fff}''',
'''<div class="top"><span>AP CS · IGCSE · IB</span><h1>Python or Java first?</h1></div>
<div class="half l"><h2>Java</h2><p>AP CSA uses a subset of Java</p></div>
<div class="half r"><h2>Python</h2><p>AP CSP names no language</p><p>IGCSE 0478: most code answers are pseudocode</p></div>
<div class="vs">VS</div><div class="win">Total beginner? Python is usually the faster start</div>
<div class="foot"><span>Syed Shahmikh Ali</span><span>shahmikh.com</span></div>''')
# 4 Quote card parents (warm, speech bubble)
pins['parents-quote']=('''body{background:#2B1A3D;color:#fff}
.q{position:absolute;top:90px;left:64px;right:64px;background:#FFE9D6;color:#2B1A3D;border-radius:60px;padding:70px 60px 80px}
.q:after{content:"";position:absolute;left:120px;bottom:-60px;border:60px solid transparent;border-top-color:#FFE9D6;border-bottom:0}
.q small{font-weight:800;font-size:30px;letter-spacing:.1em;color:#E4572E}
.q h1{font-weight:800;font-size:118px;line-height:1.02;margin-top:20px;letter-spacing:-.02em}
.q h1 em{font-style:normal;color:#E4572E;text-decoration:underline;text-decoration-thickness:10px}
.a{position:absolute;top:960px;left:64px;right:64px}
.a h3{font-weight:800;font-size:44px;color:#FFB347;margin-bottom:30px}
.a div{font-weight:700;font-size:42px;line-height:1.25;margin-bottom:26px;padding-left:70px;position:relative}
.a div:before{content:"\\2192";position:absolute;left:0;color:#FFB347;font-weight:800}
.a b{color:#FFB347}
.foot{color:#fff}.foot span:last-child{color:#FFB347}''',
'''<div class="q"><small>PARENTS, ASK YOURSELF</small><h1>Is my child learning with AI, or <em>copying</em>?</h1></div>
<div class="a"><h3>Free guide inside shahmikh.com</h3><div>25 copy-paste prompts</div><div>Prompts that give <b>hints, not answers</b></div><div>Turn class notes into quizzes</div><div>5 questions to ask your child</div></div>
<div class="foot"><span>Syed Shahmikh Ali</span><span>shahmikh.com</span></div>''')
# 5 Roadmap kids (warm path)
pins['kids-roadmap']=('''body{background:#FFE9D6;color:#2B1A3D}
.k{position:absolute;top:80px;left:64px;background:#E4572E;color:#fff;font-weight:800;font-size:30px;letter-spacing:.08em;padding:12px 28px;border-radius:40px}
h1{position:absolute;top:170px;left:64px;right:64px;font-weight:800;font-size:92px;line-height:1.02;letter-spacing:-.02em}
h1 em{font-style:normal;color:#E4572E}
.line{position:absolute;left:119px;top:560px;width:12px;height:700px;background:repeating-linear-gradient(#2B1A3D 0 22px,transparent 22px 44px);border-radius:6px}
.s{position:absolute;left:64px;right:64px;display:flex;gap:40px;align-items:center}
.s .d{flex:none;width:124px;height:124px;border-radius:50%;background:#E4572E;color:#fff;font-weight:800;font-size:60px;display:flex;align-items:center;justify-content:center;border:8px solid #FFE9D6}
.s .t{background:#fff;border-radius:28px;padding:22px 30px;font-weight:800;font-size:42px;line-height:1.15;box-shadow:0 6px 0 rgba(0,0,0,.08);flex:1}
.s .t span{display:block;font-weight:700;font-size:32px;opacity:.75;margin-top:4px}
.foot{color:#2B1A3D}''',
'''<div class="k">KIDS AI CLASS · AGES 10 TO 14</div><h1>How AI stays <em>safe</em> in class</h1><div class="line"></div>
<div class="s" style="top:520px"><div class="d">1</div><div class="t">Teacher is always there<span>AI tools are used live</span></div></div>
<div class="s" style="top:720px"><div class="d">2</div><div class="t">No personal accounts<span>Kids do not need their own</span></div></div>
<div class="s" style="top:920px"><div class="d">3</div><div class="t">Notes for parents<span>How each tool is used</span></div></div>
<div class="s" style="top:1120px"><div class="d">6</div><div class="t">Week 6: check AI answers<span>Spot the made-up ones</span></div></div>
<div class="foot"><span>Syed Shahmikh Ali</span><span>shahmikh.com</span></div>''')
for k,(c,b) in pins.items(): open(k+'.html','w').write(H%(F,F,c,b))
json.dump(list(pins),open('list.json','w'))
