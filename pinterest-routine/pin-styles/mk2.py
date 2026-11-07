import json
F='file:///home/claude/shahmikh-site/public/fonts/'
H='''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:J;font-weight:700;src:url(%splus-jakarta-sans-latin-700-normal.woff2)}
@font-face{font-family:J;font-weight:800;src:url(%splus-jakarta-sans-latin-800-normal.woff2)}
*{box-sizing:border-box;margin:0}
body{width:1000px;height:1500px;font-family:J,sans-serif;position:relative;overflow:hidden}
.foot{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-weight:800;font-size:34px}
%s</style></head><body>%s</body></html>'''
P={}
# 1 donut (AP CSP create task)
P['csp-donut']=('''body{background:#FFF4D6;color:#1E2A4A}
.k{position:absolute;top:80px;left:64px;font-weight:800;font-size:32px;letter-spacing:.1em;color:#C2410C}
h1{position:absolute;top:140px;left:64px;right:64px;font-weight:800;font-size:100px;line-height:1.02;letter-spacing:-.02em}
h1 em{font-style:normal;color:#C2410C}
.d{position:absolute;left:150px;top:520px;width:700px;height:700px;border-radius:50%;background:conic-gradient(#C2410C 0 30%,#1E2A4A 30% 100%)}
.d:after{content:"";position:absolute;inset:150px;border-radius:50%;background:#FFF4D6}
.c{position:absolute;left:150px;top:800px;width:700px;text-align:center;font-weight:800;font-size:150px;line-height:1;letter-spacing:-.03em;z-index:2}
.c small{display:block;font-size:40px;letter-spacing:0;margin-top:6px}
.l1{position:absolute;left:64px;top:1250px;font-weight:800;font-size:38px;color:#C2410C}
.l2{position:absolute;right:64px;top:1250px;font-weight:800;font-size:38px;text-align:right}
.foot{color:#1E2A4A}''',
'''<div class="k">AP COMPUTER SCIENCE PRINCIPLES</div><h1>The Create task is <em>30%</em> of your score</h1>
<div class="d"></div><div class="c">30%<small>Create task</small></div>
<div class="l1">Create task 30%</div><div class="l2">Exam 70%<br><span style="font-size:30px;opacity:.7">70 multiple-choice questions</span></div>
<div class="foot"><span>Syed Shahmikh Ali</span><span>shahmikh.com</span></div>''')
# 2 igcse paper 2 stamp: cross vs tick on notebook
P['igcse-paper2']=('''body{background:#F7F3E8;color:#1B2B2B;background-image:repeating-linear-gradient(transparent 0 69px,#CFE3EA 69px 72px)}
.k{position:absolute;top:70px;left:64px;background:#1B2B2B;color:#F7F3E8;font-weight:800;font-size:30px;padding:12px 26px;border-radius:12px}
h1{position:absolute;top:160px;left:64px;right:64px;font-weight:800;font-size:96px;line-height:1.05;letter-spacing:-.02em}
h1 em{font-style:normal;background:#FFD23F;padding:0 12px}
.card{position:absolute;left:64px;right:64px;border-radius:30px;padding:34px 40px 34px 150px;background:#fff;box-shadow:0 8px 0 rgba(0,0,0,.1)}
.card b{display:block;font-weight:800;font-size:56px;line-height:1.1}
.card span{display:block;font-weight:700;font-size:36px;margin-top:10px;opacity:.8}
.card i{position:absolute;left:36px;top:34px;width:84px;height:84px;border-radius:50%;font-style:normal;font-weight:800;font-size:56px;color:#fff;display:flex;align-items:center;justify-content:center}
.x i{background:#D7263D}.ok i{background:#1A9A5B}.x{border-left:14px solid #D7263D}.ok{border-left:14px solid #1A9A5B}
.stat{position:absolute;left:64px;right:64px;top:1120px;display:flex;gap:20px}
.stat div{flex:1;background:#1B2B2B;color:#fff;border-radius:24px;padding:24px;font-weight:700;font-size:32px;line-height:1.2}
.stat b{display:block;font-size:60px;color:#FFD23F;font-weight:800}
.foot{color:#1B2B2B}''',
'''<div class="k">IGCSE COMPUTER SCIENCE 0478 · PAPER 2</div><h1>Code answers go in <em>pseudocode</em></h1>
<div class="card x" style="top:560px"><i>&#10005;</i><b>Python, Java or VB</b><span>Code in a programming language earns no marks</span></div>
<div class="card ok" style="top:810px"><i>&#10003;</i><b>Pseudocode</b><span>Except the 15-mark scenario question, where Python, Visual Basic or Java is allowed</span></div>
<div class="stat"><div><b>75</b>marks</div><div><b>1h 45</b>minutes</div><div><b>No</b>calculator</div></div>
<div class="foot"><span>Syed Shahmikh Ali</span><span>shahmikh.com</span></div>''')
# 3 checklist notebook (past papers method)
P['past-papers-checklist']=('''body{background:#FFFDF5;color:#2A2140;background-image:repeating-linear-gradient(transparent 0 79px,#D9D2F5 79px 82px)}
body:before{content:"";position:absolute;left:110px;top:0;bottom:0;width:6px;background:#E57373}
.k{position:absolute;top:70px;left:150px;font-weight:800;font-size:32px;letter-spacing:.1em;color:#6D4AE3}
h1{position:absolute;top:130px;left:150px;right:64px;font-weight:800;font-size:92px;line-height:1.04;letter-spacing:-.02em}
h1 em{font-style:normal;color:#6D4AE3}
.it{position:absolute;left:150px;right:64px;display:flex;gap:30px;align-items:center;font-weight:800;font-size:44px;line-height:1.15}
.it i{flex:none;width:70px;height:70px;border:7px solid #2A2140;border-radius:14px;position:relative}
.it i:after{content:"";position:absolute;left:12px;top:-14px;width:22px;height:46px;border:solid #1A9A5B;border-width:0 10px 10px 0;transform:rotate(40deg)}
.it span{font-weight:700;font-size:32px;display:block;opacity:.7;margin-top:6px}
.foot{color:#2A2140;left:150px}''',
'''<div class="k">PAST PAPER METHOD</div><h1>5 steps to use past papers <em>properly</em></h1>
<div class="it" style="top:520px"><i></i><div>Mark with the official mark scheme</div></div>
<div class="it" style="top:680px"><i></i><div>Log every lost mark with a reason</div></div>
<div class="it" style="top:840px"><i></i><div>Redo weak questions after a few days</div></div>
<div class="it" style="top:1000px"><i></i><div>Read examiner reports where they exist</div></div>
<div class="it" style="top:1160px"><i></i><div>Mix timed and untimed papers</div></div>
<div class="foot"><span>Syed Shahmikh Ali</span><span>shahmikh.com</span></div>''')
# 4 diagnosis two cards
P['subject-or-habits']=('''body{background:#E8F1FF;color:#14213D}
.k{position:absolute;top:80px;left:64px;background:#2563EB;color:#fff;font-weight:800;font-size:30px;letter-spacing:.08em;padding:12px 28px;border-radius:40px}
h1{position:absolute;top:170px;left:64px;right:64px;font-weight:800;font-size:98px;line-height:1.02;letter-spacing:-.02em}
h1 em{font-style:normal;color:#2563EB}
.c{position:absolute;left:64px;right:64px;border-radius:40px;padding:44px 50px}
.c h2{font-weight:800;font-size:72px;line-height:1}
.c p{font-weight:700;font-size:42px;line-height:1.25;margin-top:16px}
.a{top:600px;background:#14213D;color:#fff}.b{top:930px;background:#fff;box-shadow:0 8px 0 rgba(0,0,0,.1)}
.a h2{color:#7DB7FF}.b h2{color:#2563EB}
.or{position:absolute;left:430px;top:840px;width:140px;height:80px;border-radius:40px;background:#FFD23F;font-weight:800;font-size:44px;display:flex;align-items:center;justify-content:center;z-index:3}
.t{position:absolute;left:64px;right:64px;top:1260px;text-align:center;font-weight:800;font-size:36px;opacity:.8}
.foot{color:#14213D}''',
'''<div class="k">PARENT GUIDE</div><h1>Subject problem or <em>study habits</em>?</h1>
<div class="c a"><h2>Content gap</h2><p>Can't explain the idea in their own words</p></div><div class="or">OR</div>
<div class="c b"><h2>Habit problem</h2><p>Knows it on the page, not under test conditions</p></div>
<div class="t">Two-week check: one topic, a few closed-notes questions</div>
<div class="foot"><span>Syed Shahmikh Ali</span><span>shahmikh.com</span></div>''')
# 5 code mockup java oop
P['java-code']=('''body{background:#0B1020;color:#E6EDF7}
.k{position:absolute;top:80px;left:64px;font-weight:800;font-size:32px;letter-spacing:.1em;color:#FFB454}
h1{position:absolute;top:140px;left:64px;right:64px;font-weight:800;font-size:100px;line-height:1.02;letter-spacing:-.02em}
h1 em{font-style:normal;color:#FFB454}
.w{position:absolute;left:64px;right:64px;top:520px;background:#141B34;border-radius:28px;box-shadow:0 20px 0 rgba(0,0,0,.35);overflow:hidden}
.bar{height:70px;background:#1D2748;display:flex;gap:14px;align-items:center;padding:0 28px}
.bar b{width:24px;height:24px;border-radius:50%;display:block}
pre{font-family:Menlo,Consolas,monospace;font-size:38px;line-height:1.6;padding:34px 40px;color:#E6EDF7;white-space:pre}
.kw{color:#C792EA}.ty{color:#82AAFF}.an{color:#FFB454}.cm{color:#7E8BB5}
.n{position:absolute;left:64px;right:64px;top:1100px;display:flex;gap:20px}
.n div{flex:1;background:#1D2748;border-radius:24px;padding:26px;font-weight:700;font-size:32px;line-height:1.25}
.n b{display:block;color:#FFB454;font-size:36px;margin-bottom:6px;font-weight:800}
.foot{color:#E6EDF7}.foot span:last-child{color:#FFB454}''',
'''<div class="k">AP CSA · JAVA OOP</div><h1>Inheritance in <em>Java</em></h1>
<div class="w"><div class="bar"><b style="background:#FF5F57"></b><b style="background:#FEBC2E"></b><b style="background:#28C840"></b></div>
<pre><span class="kw">class</span> <span class="ty">Animal</span> {
  <span class="kw">public void</span> speak() { }
}
<span class="kw">class</span> <span class="ty">Dog</span> <span class="kw">extends</span> <span class="ty">Animal</span> {
  <span class="an">@Override</span>
  <span class="kw">public void</span> speak() { }
}</pre></div>
<div class="n"><div><b>Inherits</b>public and protected members</div><div><b>Does not inherit</b>private members or constructors</div></div>
<div class="foot"><span>Syed Shahmikh Ali</span><span>shahmikh.com</span></div>''')
for k,(c,b) in P.items(): open(k+'.html','w').write(H%(F,F,c,b))
json.dump(list(P),open('list.json','w'))
