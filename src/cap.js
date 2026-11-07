const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:450}});
p.on('pageerror',e=>console.log('E:',e.message));p.on('console',m=>{const t=m.text();if(/error|ERROR/.test(t))console.log('C:',t.slice(0,600))});
const c=process.argv[2],out=process.argv[3];const fps=+(process.argv[5]||0);
await p.goto('http://localhost:8765/hero.html?c='+c);await p.waitForFunction(()=>window.ready,null,{timeout:120000});
const list=fps?[...Array(10*fps).keys()].map(i=>i/fps):(process.argv[4]||'2').split(',').map(Number);
let i=0;for(const t of list){await p.evaluate(t=>window.renderAt(t),t);await p.locator('#wrap').screenshot({path:`${out}/${String(i++).padStart(3,'0')}.png`});}
await b.close();})();
