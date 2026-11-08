(() => {
"use strict";
const ns="http://www.w3.org/2000/svg";
const edgesLayer=document.getElementById("edges"),nodesLayer=document.getElementById("nodes");
const timeline=document.getElementById("timeline"),playToggle=document.getElementById("play-toggle");
const playIcon=document.getElementById("play-icon"),playLabel=document.getElementById("play-label");
const sceneIndex=document.getElementById("scene-index"),sceneKicker=document.getElementById("scene-kicker");
const sceneCaption=document.getElementById("scene-caption"),timeReadout=document.getElementById("time-readout");
const chapterButtons=[...document.querySelectorAll(".chapter")];
const reducedMotion=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const duration=54;
const chapters=[
{start:0,end:18,kicker:"THE GENESIS",caption:"Before connection, there is only possibility."},
{start:18,end:38,kicker:"THE CONVERGENCE",caption:"Relations begin to shape a field of signals."},
{start:38,end:54,kicker:"THE EMERGENCE",caption:"A larger pattern becomes visible."}
];
const nodes=Array.from({length:42},(_,i)=>{
const angle=i*2.3999632297,radius=55+((i*37)%170);
return{x:450+Math.cos(angle)*radius*1.72,y:280+Math.sin(angle)*radius,phase:i*.37,r:1.7+(i%4)*.48};
});
const pairs=[];
nodes.forEach((a,i)=>nodes.forEach((b,j)=>{if(j>i&&Math.hypot(a.x-b.x,a.y-b.y)<112&&(i+j)%3===0)pairs.push([i,j]);}));
const edgeEls=pairs.map(([a,b])=>{const el=document.createElementNS(ns,"line");el.setAttribute("class","edge");edgesLayer.appendChild(el);return{el,a,b};});
const nodeEls=nodes.map((n,i)=>{const el=document.createElementNS(ns,"circle");el.setAttribute("class",i===0?"node node-core":"node");el.setAttribute("r",n.r);nodesLayer.appendChild(el);return el;});
let currentTime=0,playing=!reducedMotion,lastStamp=0,frameId=0;
function clamp(v,min,max){return Math.max(min,Math.min(max,v));}
function smooth(a,b,x){const t=clamp((x-a)/(b-a),0,1);return t*t*(3-2*t);}
function chapterAt(t){return t<18?0:t<38?1:2;}
function formatTime(t){return"00:"+String(Math.floor(t)).padStart(2,"0");}
function updateText(){
const i=chapterAt(currentTime),c=chapters[i];
sceneIndex.textContent=String(i+1).padStart(2,"0");sceneKicker.textContent=c.kicker;sceneCaption.textContent=c.caption;
chapterButtons.forEach((b,j)=>b.classList.toggle("active",j===i));
timeline.value=String(currentTime);timeReadout.textContent=formatTime(currentTime)+" / 00:54";
}
function render(t){
const convergence=smooth(10,31,t),emergence=smooth(31,49,t),organization=convergence*.55+emergence*.45;
nodes.forEach((n,i)=>{
const pull=organization*.46,pulse=1+Math.sin(t*.8+n.phase)*.12;
const x=n.x+(450-n.x)*pull+Math.cos(t*.23+n.phase)*7*(1-organization*.5);
const y=n.y+(280-n.y)*pull+Math.sin(t*.28+n.phase)*6*(1-organization*.5);
nodeEls[i].setAttribute("cx",x.toFixed(2));nodeEls[i].setAttribute("cy",y.toFixed(2));
nodeEls[i].setAttribute("r",(n.r*pulse*(1+emergence*.3)).toFixed(2));
nodeEls[i].style.opacity=String(.25+organization*.65+Math.sin(t*.7+n.phase)*.1);
});
edgeEls.forEach(({el,a,b},i)=>{
const na=nodeEls[a],nb=nodeEls[b];
el.setAttribute("x1",na.getAttribute("cx"));el.setAttribute("y1",na.getAttribute("cy"));
el.setAttribute("x2",nb.getAttribute("cx"));el.setAttribute("y2",nb.getAttribute("cy"));
el.style.opacity=String(.04+convergence*.28+emergence*.23+(i%7)/35);
});
}
function setTime(t){currentTime=clamp(t,0,duration);updateText();render(currentTime);}
function setPlaying(value){
playing=Boolean(value)&&!reducedMotion;playIcon.textContent=playing?"Ⅱ":"▶";playLabel.textContent=playing?"PAUSE":"PLAY";
if(playing&&!frameId)frameId=requestAnimationFrame(tick);
}
function tick(stamp){
frameId=0;if(!playing)return;if(!lastStamp)lastStamp=stamp;
currentTime+=Math.min((stamp-lastStamp)/1000,.08);lastStamp=stamp;
if(currentTime>=duration){currentTime=duration;setPlaying(false);lastStamp=0;}
updateText();render(currentTime);if(playing)frameId=requestAnimationFrame(tick);
}
chapterButtons.forEach(button=>button.addEventListener("click",()=>{
setTime(chapters[Number(button.dataset.scene)].start);setPlaying(false);
}));
timeline.addEventListener("input",()=>{setTime(Number(timeline.value));setPlaying(false);});
playToggle.addEventListener("click",()=>{
if(!playing&&currentTime>=duration)setTime(0);lastStamp=0;setPlaying(!playing);
});
setTime(0);if(!reducedMotion)setPlaying(true);
})();
