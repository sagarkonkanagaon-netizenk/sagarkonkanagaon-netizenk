const {chromium}=require('playwright');
// node capx.js page.html outdir "t1,t2" [w]   |  node capx.js page.html outdir fps:15:12 [w]
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const w=+(process.argv[5]||1600);
const p=await b.newPage({viewport:{width:w,height:+(process.argv[6]||w/4)}});
p.on('pageerror',e=>console.log('E:',e.message));p.on('console',m=>{const t=m.text();if(/error|ERROR|LOG/.test(t))console.log('C:',t.slice(0,600))});
const pg=process.argv[2],out=process.argv[3],spec=process.argv[4];
await p.goto(`http://localhost:8765/${pg}?w=${w}`);await p.waitForFunction(()=>window.ready,null,{timeout:180000});
let list;if(spec.startsWith('fps:')){const [,f,d]=spec.split(':').map(Number);list=[...Array(Math.round(f*d)).keys()].map(i=>i/f);}else list=spec.split(',').map(Number);
const t0=Date.now();let i=0;for(const t of list){await p.evaluate(t=>window.renderAt(t),t);await p.locator('#wrap').screenshot({path:`${out}/${String(i++).padStart(3,'0')}.png`});}
console.log('frames',i,'ms/frame',Math.round((Date.now()-t0)/i));
await b.close();})();
