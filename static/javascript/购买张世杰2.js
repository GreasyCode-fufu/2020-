window.onload=function(){
    var ip=document.getElementById("ip");
    var ipm=document.getElementById("ipm");
    var sms=document.getElementById("sms");
    var ys=document.getElementById("ys");
    var js=document.getElementById("js");
    var hls=document.getElementById("hls");  
    var ote=document.getElementById("ote");
    var tfs=document.getElementById("tfs");
    var foe=document.getElementById("foe");  


    ip.onclick=oip;
    ipm.onclick=oipm;
    sms.onclick=osms;
    ys.onclick=oys;
    js.onclick=ojs;
    hls.onclick=ohls;
    ote.onclick=oote;
    tfs.onclick=otfs;
    foe.onclick=ofoe;

    function oip(){
        ip.style.boxShadow="0 0 2px 2px #aaeeee";
        ipm.style.boxShadow="0 0 2px 2px #ffffff";
    }
    function oipm(){
        ipm.style.boxShadow="0 0 2px 2px #aaeeee";
        ip.style.boxShadow="0 0 2px 2px #ffffff";
    }

    function osms(){
        sms.style.boxShadow="0 0 2px 2px #aaeeee";
        ys.style.boxShadow="0 0 2px 2px #ffffff";
        js.style.boxShadow="0 0 2px 2px #ffffff";
        hls.style.boxShadow="0 0 2px 2px #ffffff";
    }
    function oys(){
        ys.style.boxShadow="0 0 2px 2px #aaeeee";
        sms.style.boxShadow="0 0 2px 2px #ffffff";
        js.style.boxShadow="0 0 2px 2px #ffffff";
        hls.style.boxShadow="0 0 2px 2px #ffffff";
    }
    function ojs(){
        js.style.boxShadow="0 0 2px 2px #aaeeee";
        ys.style.boxShadow="0 0 2px 2px #ffffff";
        sms.style.boxShadow="0 0 2px 2px #ffffff";
        hls.style.boxShadow="0 0 2px 2px #ffffff";
    }
    function ohls(){
        hls.style.boxShadow="0 0 2px 2px #aaeeee";
        ys.style.boxShadow="0 0 2px 2px #ffffff";
        js.style.boxShadow="0 0 2px 2px #ffffff";
        sms.style.boxShadow="0 0 2px 2px #ffffff";
    }

    function oote(){
        ote.style.boxShadow="0 0 2px 2px #aaeeee";
        tfs.style.boxShadow="0 0 2px 2px #ffffff";
        foe.style.boxShadow="0 0 2px 2px #ffffff";
    }
    function otfs(){
        tfs.style.boxShadow="0 0 2px 2px #aaeeee";
        ote.style.boxShadow="0 0 2px 2px #ffffff";
        foe.style.boxShadow="0 0 2px 2px #ffffff";
    }
    function ofoe(){
        foe.style.boxShadow="0 0 2px 2px #aaeeee";
        ote.style.boxShadow="0 0 2px 2px #ffffff";
        tfs.style.boxShadow="0 0 2px 2px #ffffff";
    }
}