import json
FONT='file:///home/claude/shahmikh-site/public/fonts/'
pins=[
 dict(f='kids-weekly',kicker='Ages 10 to 14 · AI Explorers',title='What your child does each week in our AI program',
      items=[('60 min','Live class with a real teacher'),('45 min','Optional build clinic to get help'),('Weekly','A project your child can show you'),('Parents','A short update on what they learned')]),
 dict(f='kids-ai-safe',kicker='AI and kids',title='How AI is used safely in class',
      items=[('Live','AI tools are used with the teacher present'),('No accounts','Children do not need personal AI accounts'),('Parents','A short note on how each tool is used'),('Week 6','Kids learn to check AI answers and spot made-up ones')]),
 dict(f='guide-parents',kicker='Free guide for parents',title='Is your child using AI to learn, or to copy?',
      items=[('25','copy-paste prompts in the free guide'),('Hints','Prompts that give hints, not answers'),('Test','Turn notes into quizzes and flashcards'),('Parents','Five questions to ask about AI use')]),
]
tpl=open('t.html').read()
for p in pins:
    li=''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a,b in p['items'])
    open(p['f']+'.html','w').write(tpl.replace('%FONT%',FONT).replace('%KICK%',p['kicker']).replace('%TITLE%',p['title']).replace('%LI%',li))
json.dump([p['f'] for p in pins],open('list.json','w'))
