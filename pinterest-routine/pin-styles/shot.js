const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1000,height:1500}});
for(const f of JSON.parse(fs.readFileSync('list.json'))){await p.goto('file://'+process.cwd()+'/'+f+'.html');await p.waitForTimeout(500);await p.screenshot({path:f+'.png'});}
await b.close()})();
