let menu1=document.getElementById('menu1');
let menu2=document.getElementById('menu2');
let menu3=document.getElementById('menu3');
let menu4=document.getElementById('menu4');
let menu5=document.getElementById('menu5');
let menu6=document.getElementById('menu6');
let menu7=document.getElementById('menu7');

let left_bottom2=document.getElementById('left_bottom2');
let left_bottom3=document.getElementById('left_bottom3');
let left_bottom4=document.getElementById('left_bottom4');
let left_bottom5=document.getElementById('left_bottom5');
let left_bottom6=document.getElementById('left_bottom6');

let child_menu2=document.getElementById('child_menu2');
let child_menu3=document.getElementById('child_menu3');
let child_menu4=document.getElementById('child_menu4');
let child_menu5=document.getElementById('child_menu5');
let child_menu6=document.getElementById('child_menu6');

let i=0;
menu6.onclick=function(){
    i++;
    if(i%2==1){
        left_bottom6.style.transform="rotate(90deg)";
        left_bottom6.style.marginTop="15px";
        child_menu6.style.height="5rem";
    }
    else{
        left_bottom6.style.transform="rotate(0)";
        left_bottom6.style.marginTop="12px";
        child_menu6.style.height="0rem";
    }
}
menu5.onclick=function(){
    i++;
    if(i%2==1){
        left_bottom5.style.transform="rotate(90deg)";
        left_bottom5.style.marginTop="15px";
        child_menu5.style.height="5rem";
    }
    else{
        left_bottom5.style.transform="rotate(0)";
        left_bottom5.style.marginTop="12px";
        child_menu5.style.height="0rem";
    }
}
menu4.onclick=function(){
    i++;
    if(i%2==1){
        left_bottom4.style.transform="rotate(90deg)";
        left_bottom4.style.marginTop="15px";
        child_menu4.style.height="5rem";
    }
    else{
        left_bottom4.style.transform="rotate(0)";
        left_bottom4.style.marginTop="12px";
        child_menu4.style.height="0rem";
    }
}
menu3.onclick=function(){
    i++;
    if(i%2==1){
        left_bottom3.style.transform="rotate(90deg)";
        left_bottom3.style.marginTop="15px";
        child_menu3.style.height="5rem";
    }
    else{
        left_bottom3.style.transform="rotate(0)";
        left_bottom3.style.marginTop="12px";
        child_menu3.style.height="0rem";
    }
}
menu2.onclick=function(){
    i++;
    if(i%2==1){
        left_bottom2.style.transform="rotate(90deg)";
        left_bottom2.style.marginTop="15px";
        child_menu2.style.height="7.5rem";
    }
    else{
        left_bottom2.style.transform="rotate(0)";
        left_bottom2.style.marginTop="12px";
        child_menu2.style.height="0rem";
    }
}