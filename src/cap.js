const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:450}});
p.on('console',m=>console.log('C:',m.text()));p.on('pageerror',e=>console.log('E:',e.message));
await p.goto('http://localhost:8765/reveal.html');await p.waitForFunction(()=>window.ready,null,{timeout:120000});
const times=(process.argv[2]||'0,1.5,3').split(',').map(Number);const fps=+(process.argv[3]||0);
const list=fps?[...Array(10*fps).keys()].map(i=>i/fps):times;
let i=0;for(const t of list){const t0=Date.now();await p.evaluate(t=>window.renderAt(t),t);
 await p.locator('#wrap').screenshot({path:`f/${String(i++).padStart(3,'0')}.png`});if(i==1)console.log('ms',Date.now()-t0);}
await b.close();})();
