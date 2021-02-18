var btn=document.getElementById("btn");
var obtn=document.getElementById("obtn");
btn.onclick=sidebar;
obtn.onclick=osidebar;

function sidebar(){
    var sidebar=document.getElementById("sidebar");
    sidebar.style.minWidth="13rem";
    sidebar.style.minHeight="20rem";
    btn.style.zIndex=1;
    btn.style.opacity=0;
    obtn.style.zIndex=2;
    obtn.style.opacity=1;
}
function osidebar(){
    var sidebar=document.getElementById("sidebar");
    sidebar.style.minWidth="0rem";
    sidebar.style.minHeight="0rem";
    btn.style.zIndex=2;
    btn.style.opacity=1;
    obtn.style.zIndex=1;
    obtn.style.opacity=0;
}


