const API_BASE_URL = window.API_BASE_URL || "";
const promptEl=document.getElementById("prompt"), run=document.getElementById("run");
const architecture=document.getElementById("architecture"), tasks=document.getElementById("tasks"), memory=document.getElementById("memory");
const steps=[...document.querySelectorAll(".step")];

function demo(prompt,stack){
 return {stack:{frontend:"Next.js + TypeScript",backend:stack==="go"?"Go + REST API":"FastAPI",database:"PostgreSQL"},requirements:["Requirements analysis","Responsive UI","API layer","Persistent memory","Automated tests"],architecture:["Frontend dashboard","Agent orchestration","Tool/API layer","Project memory","Test & security"],tasks:[
{id:"T-01",title:"Requirements",detail:"Convert the brief into explicit functional and non-functional requirements."},
{id:"T-02",title:"Architecture",detail:"Design clean frontend, backend, data and integration boundaries."},
{id:"T-03",title:"Implementation",detail:"Generate modules, contracts, validation and error handling."},
{id:"T-04",title:"Testing",detail:"Create unit, integration and API test coverage."},
{id:"T-05",title:"Security review",detail:"Review authentication, secrets, validation and API risks."},
{id:"T-06",title:"Deployment",detail:"Prepare environment variables, CI and deployment configuration."}],memory:{project_goal:prompt,decisions:["Stack: "+stack],facts:["Context is stored as structured project memory."]}};
}
async function generate(){
 const prompt=promptEl.value.trim(); if(!prompt){promptEl.focus();return}
 run.disabled=true;run.textContent="Agent is thinking…";
 steps.forEach((s,i)=>{s.classList.toggle("active",i===0)});
 let data;
 try{
   if(API_BASE_URL){
    const r=await fetch(API_BASE_URL+"/agent/plan",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({prompt,stack:document.getElementById("stack").value})});
    if(!r.ok)throw new Error();
    data=await r.json(); document.getElementById("apiState").textContent="LIVE API";
   }else throw new Error();
 }catch(e){data=demo(prompt,document.getElementById("stack").value);document.getElementById("apiState").textContent="DEMO ENGINE"}
 architecture.innerHTML=data.architecture.map((x,i)=>`<div class="arch-node">0${i+1}<span>${x}</span></div>`).join("");
 tasks.innerHTML=data.tasks.map(t=>`<div class="task"><b>${t.id}</b><div><p>${t.title}</p><small>${t.detail}</small></div></div>`).join("");
 memory.textContent=JSON.stringify(data.memory,null,2);
 steps.forEach((s,i)=>setTimeout(()=>s.classList.toggle("active",true),i*180));
 run.disabled=false;run.innerHTML="Generate engineering plan <b>→</b>";
}
run.addEventListener("click",generate);
promptEl.addEventListener("keydown",e=>{if((e.ctrlKey||e.metaKey)&&e.key==="Enter")generate()});
