var p1=document.getElementsByName("p1");
var d=document.getElementsByName("d");
var d1=document.getElementById('d1');
var d2=document.getElementById('d2');
var d3=document.getElementById('d3');
var d4=document.getElementById('d4');
var p2=document.getElementById('p2');
var p02=document.getElementsByName("p2");
var p4=document.getElementsByName("p4");
var p3=document.getElementsByName("p3");
var div3222=document.getElementById('div3222');
var div3221=document.getElementById('div3221');
var other1=document.getElementById('other1');
for(let i=0;i<p1.length;i++){
    // console.log(p1[i]);
    p1[i].onclick=function(){
        // console.log(p1[i].innerText);
        if(p1[i].innerText==="河南省"){
            // console.log('正确')
            for(let j=0;j<d.length;j++){
                // console.log('正确');
                d[j].style.transform=`translateY(-8rem)`;
                d1.style.backgroundColor="#dddddd";
                d2.style.backgroundColor="#ffffff";
                d3.style.backgroundColor="#dddddd";
                d4.style.backgroundColor="#dddddd";
                p2.innerText=p1[i].innerText+"/";
                a();
            }
        }
    }
}
function a(){
    // console.log('链接成功');
    for(let i=0;i<p02.length;i++){
        // console.log(p1[i]);
        p02[i].onclick=function(){
            // console.log('true');
            if(p02[i].innerText==="新乡市"||p02[i].innerText==="周口市"){
                // console.log('true');
                d1.style.backgroundColor="#dddddd";
                d2.style.backgroundColor="#dddddd";
                d3.style.backgroundColor="#ffffff";
                d4.style.backgroundColor="#dddddd";
                if(p02[i].innerText==="新乡市"){
                    for(let j=0;j<d.length;j++){
                        d[j].style.transform=`translateY(-16rem)`;
                        p2.innerText=p02[i].innerText+"/";
                        b();
                    } 
                }else{
                    for(let j=0;j<d.length;j++){
                        d[j].style.transform=`translateY(-32rem)`;
                        p2.innerText=p02[i].innerText+"/";
                    } 
                }
            }
        }
    }
}
function b(){
    for(let i=0;i<p3.length;i++){
        // console.log(p3[i].innerText);
        p3[i].onclick=function(){
            // console.log(p3[i].innerText);
            if(p3[i].innerText==="牧野区"){
                // console.log('true');
                for(let j=0;j<d.length;j++){
                    d[j].style.transform=`translateY(-24rem)`;
                    p2.innerText=p3[i].innerText+"/";
                }  
                d1.style.backgroundColor="#dddddd";
                d2.style.backgroundColor="#dddddd";
                d3.style.backgroundColor="#dddddd";
                d4.style.backgroundColor="#ffffff";
                c();
            }
        }
    }
}
function c(){
    for(let i=0;i<p4.length;i++){
        p4[i].onclick=function(){
            // console.log('true');
            p2.innerText=p4[i].innerText;
            d1.style.backgroundColor="#ffffff";
            d2.style.backgroundColor="#dddddd";
            d3.style.backgroundColor="#dddddd";
            d4.style.backgroundColor="#dddddd";
            for(let j=0;j<d.length;j++){
                d[j].style.transform=`translateY(0)`;
            } 
            div3222.style.display="none";
        }
    }
}
other1.onmouseover=function(){
    // console.log(other1);
    div3222.style.display="flex";
}
div32222.onmouseout=function(){
    div3222.style.display="none";
    console.log('离开');
}