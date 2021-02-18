var shut_down=document.getElementById("shut_down");
var pay=document.getElementById("pay");
var buy=document.getElementById("buy");

shut_down.onclick=function shut(){
    pay.style.display="none";
}

buy.onclick=function open(){
    pay.style.display="block";
}