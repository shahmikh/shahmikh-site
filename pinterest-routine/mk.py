import json,os
FONT='file:///home/claude/shahmikh-site/public/fonts/'
pins=[
 dict(f='python-java',kicker='AP CS · IGCSE · IB',title='Python or Java as a first language?',
      items=[('AP CSA','uses a subset of Java'),('AP CSP','names no language, no coding experience needed'),('IGCSE 0478','most code answers are pseudocode'),('Beginner?','Python is usually the faster start; Java is a great second language')]),
 dict(f='past-papers',kicker='Revision method',title='Use past papers the right way',
      items=[('1','Attempt the paper'),('2','Mark it with the official mark scheme'),('3','Log every lost mark with a reason'),('4','Redo the weak questions after a few days')]),
 dict(f='security-plus',kicker='CompTIA Security+ SY0-701',title='Security+ in 8 weeks: where the marks are',
      items=[('90 questions','in 90 minutes, pass mark 750 of 900'),('28%','Security Operations'),('22%','Threats, Vulnerabilities and Mitigations'),('Tip','Study in proportion to the domain weights')]),
 dict(f='ccna',kicker='Cisco CCNA 200-301',title='CCNA: what is actually on the exam',
      items=[('25%','IP Connectivity (routing, OSPF)'),('20%','Network Fundamentals'),('20%','Network Access'),('Note','v1.1 last test date: 2 Feb 2027')]),
 dict(f='ai-prompts',kicker='Study smarter with AI',title='Stop asking AI for the answer. Ask it to test you.',
      items=[('1','Quiz me, one question at a time'),('2','Mark my work against the mark scheme'),('3','Let me explain it back, tell me what is missing'),('4','Turn my mistakes into questions to retry in 3 days')]),
]
tpl=open('t.html').read()
for p in pins:
    li=''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a,b in p['items'])
    h=tpl.replace('%FONT%',FONT).replace('%KICK%',p['kicker']).replace('%TITLE%',p['title']).replace('%LI%',li)
    open(p['f']+'.html','w').write(h)
json.dump([p['f'] for p in pins],open('list.json','w'))
