/* 菜单栏 */
let sjsp            =   document.getElementById('sjsp');
let xjsp            =   document.getElementById('xjsp');
let xgspxx          =   document.getElementById('xgspxx');

let hplb            =   document.getElementById('hplb');
let sfchz           =   document.getElementById('sfchz');

let cgrkd           =   document.getElementById('cgrkd');
let xsthrkd         =   document.getElementById('xsthrkd');

let xsckd           =   document.getElementById('xsckd');
let cgthckd         =   document.getElementById('cgthckd');

let kctbd           =   document.getElementById('kctbd');
let kctbjl          =   document.getElementById('kctbjl');

/* 菜单栏对应的主体部分 */
let sy              =   document.getElementById('sy');

let switch_sjsp     =   document.getElementById('switch_sjsp');
let switch_xjsp     =   document.getElementById('switch_xjsp');
let switch_xgspxx   =   document.getElementById('switch_xgspxx');

let switch_splb     =   document.getElementById('switch_splb');
let switch_sfchz    =   document.getElementById('switch_sfchz');

let switch_cgrkd    =   document.getElementById('switch_cgrkd');
let switch_xsthrkd  =   document.getElementById('switch_xsthrkd');

let switch_xsckd    =   document.getElementById('switch_xsckd');
let switch_cgthckd  =   document.getElementById('switch_cgthckd');

let switch_kctbd    =   document.getElementById('switch_kctbd');
let switch_kctbjl   =   document.getElementById('switch_kctbjl');

/* 跳转首页 */
menu1.onclick=function(){
    sy.style.opacity="1";
    switch_sjsp.style.opacity="0";
    switch_xjsp.style.opacity="0";
    switch_xgspxx.style.opacity="0";
    switch_splb.style.opacity="0";
    switch_sfchz.style.opacity="0";
    switch_cgrkd.style.opacity="0";
    switch_xsthrkd.style.opacity="0";
    switch_xsckd.style.opacity="0";
    switch_cgthckd.style.opacity="0";
    switch_kctbd.style.opacity="0";
    switch_kctbjl.style.opacity="0";

    sy.style.zIndex="12";
    switch_sjsp.style.zIndex="11";
    switch_xjsp.style.zIndex="10";
    switch_xgspxx.style.zIndex="9";
    switch_splb.style.zIndex="8";
    switch_sfchz.style.zIndex="7";
    switch_cgrkd.style.zIndex="6";
    switch_xsthrkd.style.zIndex="5";
    switch_xsckd.style.zIndex="4";
    switch_cgthckd.style.zIndex="3";
    switch_kctbd.style.zIndex="2";
    switch_kctbjl.style.zIndex="1";
}

/* 跳转上架商品 */
sjsp.onclick=function(){
    sy.style.opacity="0";
    switch_sjsp.style.opacity="1";
    switch_xjsp.style.opacity="0";
    switch_xgspxx.style.opacity="0";
    switch_splb.style.opacity="0";
    switch_sfchz.style.opacity="0";
    switch_cgrkd.style.opacity="0";
    switch_xsthrkd.style.opacity="0";
    switch_xsckd.style.opacity="0";
    switch_cgthckd.style.opacity="0";
    switch_kctbd.style.opacity="0";
    switch_kctbjl.style.opacity="0";

    sy.style.zIndex="1";
    switch_sjsp.style.zIndex="12";
    switch_xjsp.style.zIndex="11";
    switch_xgspxx.style.zIndex="10";
    switch_splb.style.zIndex="9";
    switch_sfchz.style.zIndex="8";
    switch_cgrkd.style.zIndex="7";
    switch_xsthrkd.style.zIndex="6";
    switch_xsckd.style.zIndex="5";
    switch_cgthckd.style.zIndex="4";
    switch_kctbd.style.zIndex="3";
    switch_kctbjl.style.zIndex="2";
}

/* 跳转下架商品 */
xjsp.onclick=function(){
    sy.style.opacity="0";
    switch_sjsp.style.opacity="0";
    switch_xjsp.style.opacity="1";
    switch_xgspxx.style.opacity="0";
    switch_splb.style.opacity="0";
    switch_sfchz.style.opacity="0";
    switch_cgrkd.style.opacity="0";
    switch_xsthrkd.style.opacity="0";
    switch_xsckd.style.opacity="0";
    switch_cgthckd.style.opacity="0";
    switch_kctbd.style.opacity="0";
    switch_kctbjl.style.opacity="0";

    sy.style.zIndex="2";
    switch_sjsp.style.zIndex="1";
    switch_xjsp.style.zIndex="12";
    switch_xgspxx.style.zIndex="11";
    switch_splb.style.zIndex="10";
    switch_sfchz.style.zIndex="9";
    switch_cgrkd.style.zIndex="8";
    switch_xsthrkd.style.zIndex="7";
    switch_xsckd.style.zIndex="6";
    switch_cgthckd.style.zIndex="5";
    switch_kctbd.style.zIndex="4";
    switch_kctbjl.style.zIndex="3";
}

/* 跳转修改商品信息 */
xgspxx.onclick=function(){
    sy.style.opacity="0";
    switch_sjsp.style.opacity="0";
    switch_xjsp.style.opacity="0";
    switch_xgspxx.style.opacity="1";
    switch_splb.style.opacity="0";
    switch_sfchz.style.opacity="0";
    switch_cgrkd.style.opacity="0";
    switch_xsthrkd.style.opacity="0";
    switch_xsckd.style.opacity="0";
    switch_cgthckd.style.opacity="0";
    switch_kctbd.style.opacity="0";
    switch_kctbjl.style.opacity="0";

    sy.style.zIndex="3";
    switch_sjsp.style.zIndex="2";
    switch_xjsp.style.zIndex="1";
    switch_xgspxx.style.zIndex="12";
    switch_splb.style.zIndex="11";
    switch_sfchz.style.zIndex="10";
    switch_cgrkd.style.zIndex="9";
    switch_xsthrkd.style.zIndex="8";
    switch_xsckd.style.zIndex="7";
    switch_cgthckd.style.zIndex="6";
    switch_kctbd.style.zIndex="5";
    switch_kctbjl.style.zIndex="4";
}

/* 跳转商品列表 */
hplb.onclick=function(){
    sy.style.opacity="0";
    switch_sjsp.style.opacity="0";
    switch_xjsp.style.opacity="0";
    switch_xgspxx.style.opacity="0";
    switch_splb.style.opacity="1";
    switch_sfchz.style.opacity="0";
    switch_cgrkd.style.opacity="0";
    switch_xsthrkd.style.opacity="0";
    switch_xsckd.style.opacity="0";
    switch_cgthckd.style.opacity="0";
    switch_kctbd.style.opacity="0";
    switch_kctbjl.style.opacity="0";

    sy.style.zIndex="4";
    switch_sjsp.style.zIndex="3";
    switch_xjsp.style.zIndex="2";
    switch_xgspxx.style.zIndex="1";
    switch_splb.style.zIndex="12";
    switch_sfchz.style.zIndex="11";
    switch_cgrkd.style.zIndex="10";
    switch_xsthrkd.style.zIndex="9";
    switch_xsckd.style.zIndex="8";
    switch_cgthckd.style.zIndex="7";
    switch_kctbd.style.zIndex="6";
    switch_kctbjl.style.zIndex="5";
}

/* 跳转收发存汇总 */
sfchz.onclick=function(){
    sy.style.opacity="0";
    switch_sjsp.style.opacity="0";
    switch_xjsp.style.opacity="0";
    switch_xgspxx.style.opacity="0";
    switch_splb.style.opacity="0";
    switch_sfchz.style.opacity="1";
    switch_cgrkd.style.opacity="0";
    switch_xsthrkd.style.opacity="0";
    switch_xsckd.style.opacity="0";
    switch_cgthckd.style.opacity="0";
    switch_kctbd.style.opacity="0";
    switch_kctbjl.style.opacity="0";

    sy.style.zIndex="5";
    switch_sjsp.style.zIndex="4";
    switch_xjsp.style.zIndex="3";
    switch_xgspxx.style.zIndex="2";
    switch_splb.style.zIndex="1";
    switch_sfchz.style.zIndex="12";
    switch_cgrkd.style.zIndex="11";
    switch_xsthrkd.style.zIndex="10";
    switch_xsckd.style.zIndex="9";
    switch_cgthckd.style.zIndex="8";
    switch_kctbd.style.zIndex="7";
    switch_kctbjl.style.zIndex="6";
}

/* 跳转采购入库单 */
cgrkd.onclick=function(){
    sy.style.opacity="0";
    switch_sjsp.style.opacity="0";
    switch_xjsp.style.opacity="0";
    switch_xgspxx.style.opacity="0";
    switch_splb.style.opacity="0";
    switch_sfchz.style.opacity="0";
    switch_cgrkd.style.opacity="1";
    switch_xsthrkd.style.opacity="0";
    switch_xsckd.style.opacity="0";
    switch_cgthckd.style.opacity="0";
    switch_kctbd.style.opacity="0";
    switch_kctbjl.style.opacity="0";

    sy.style.zIndex="6";
    switch_sjsp.style.zIndex="5";
    switch_xjsp.style.zIndex="4";
    switch_xgspxx.style.zIndex="3";
    switch_splb.style.zIndex="2";
    switch_sfchz.style.zIndex="1";
    switch_cgrkd.style.zIndex="12";
    switch_xsthrkd.style.zIndex="11";
    switch_xsckd.style.zIndex="10";
    switch_cgthckd.style.zIndex="9";
    switch_kctbd.style.zIndex="8";
    switch_kctbjl.style.zIndex="7";
}

/* 跳转销售退货入库单 */
xsthrkd.onclick=function(){
    sy.style.opacity="0";
    switch_sjsp.style.opacity="0";
    switch_xjsp.style.opacity="0";
    switch_xgspxx.style.opacity="0";
    switch_splb.style.opacity="0";
    switch_sfchz.style.opacity="0";
    switch_cgrkd.style.opacity="0";
    switch_xsthrkd.style.opacity="1";
    switch_xsckd.style.opacity="0";
    switch_cgthckd.style.opacity="0";
    switch_kctbd.style.opacity="0";
    switch_kctbjl.style.opacity="0";

    sy.style.zIndex="7";
    switch_sjsp.style.zIndex="6";
    switch_xjsp.style.zIndex="5";
    switch_xgspxx.style.zIndex="4";
    switch_splb.style.zIndex="3";
    switch_sfchz.style.zIndex="2";
    switch_cgrkd.style.zIndex="1";
    switch_xsthrkd.style.zIndex="12";
    switch_xsckd.style.zIndex="11";
    switch_cgthckd.style.zIndex="10";
    switch_kctbd.style.zIndex="9";
    switch_kctbjl.style.zIndex="8";
}

/* 跳转销售出库单 */
xsckd.onclick=function(){
    sy.style.opacity="0";
    switch_sjsp.style.opacity="0";
    switch_xjsp.style.opacity="0";
    switch_xgspxx.style.opacity="0";
    switch_splb.style.opacity="0";
    switch_sfchz.style.opacity="0";
    switch_cgrkd.style.opacity="0";
    switch_xsthrkd.style.opacity="0";
    switch_xsckd.style.opacity="1";
    switch_cgthckd.style.opacity="0";
    switch_kctbd.style.opacity="0";
    switch_kctbjl.style.opacity="0";

    sy.style.zIndex="8";
    switch_sjsp.style.zIndex="7";
    switch_xjsp.style.zIndex="6";
    switch_xgspxx.style.zIndex="5";
    switch_splb.style.zIndex="4";
    switch_sfchz.style.zIndex="3";
    switch_cgrkd.style.zIndex="2";
    switch_xsthrkd.style.zIndex="1";
    switch_xsckd.style.zIndex="12";
    switch_cgthckd.style.zIndex="11";
    switch_kctbd.style.zIndex="10";
    switch_kctbjl.style.zIndex="9";
}

/* 跳转采购退货出库单 */
cgthckd.onclick=function(){
    sy.style.opacity="0";
    switch_sjsp.style.opacity="0";
    switch_xjsp.style.opacity="0";
    switch_xgspxx.style.opacity="0";
    switch_splb.style.opacity="0";
    switch_sfchz.style.opacity="0";
    switch_cgrkd.style.opacity="0";
    switch_xsthrkd.style.opacity="0";
    switch_xsckd.style.opacity="0";
    switch_cgthckd.style.opacity="1";
    switch_kctbd.style.opacity="0";
    switch_kctbjl.style.opacity="0";

    sy.style.zIndex="9";
    switch_sjsp.style.zIndex="8";
    switch_xjsp.style.zIndex="7";
    switch_xgspxx.style.zIndex="6";
    switch_splb.style.zIndex="5";
    switch_sfchz.style.zIndex="4";
    switch_cgrkd.style.zIndex="3";
    switch_xsthrkd.style.zIndex="2";
    switch_xsckd.style.zIndex="1";
    switch_cgthckd.style.zIndex="12";
    switch_kctbd.style.zIndex="11";
    switch_kctbjl.style.zIndex="10";
}

/* 跳转库存挑拨单 */
kctbd.onclick=function(){
    sy.style.opacity="0";
    switch_sjsp.style.opacity="0";
    switch_xjsp.style.opacity="0";
    switch_xgspxx.style.opacity="0";
    switch_splb.style.opacity="0";
    switch_sfchz.style.opacity="0";
    switch_cgrkd.style.opacity="0";
    switch_xsthrkd.style.opacity="0";
    switch_xsckd.style.opacity="0";
    switch_cgthckd.style.opacity="0";
    switch_kctbd.style.opacity="1";
    switch_kctbjl.style.opacity="0";

    sy.style.zIndex="10";
    switch_sjsp.style.zIndex="9";
    switch_xjsp.style.zIndex="8";
    switch_xgspxx.style.zIndex="7";
    switch_splb.style.zIndex="6";
    switch_sfchz.style.zIndex="5";
    switch_cgrkd.style.zIndex="4";
    switch_xsthrkd.style.zIndex="3";
    switch_xsckd.style.zIndex="2";
    switch_cgthckd.style.zIndex="1";
    switch_kctbd.style.zIndex="12";
    switch_kctbjl.style.zIndex="11";
}

/* 跳转库存挑拨记录 */
kctbjl.onclick=function(){
    sy.style.opacity="0";
    switch_sjsp.style.opacity="0";
    switch_xjsp.style.opacity="0";
    switch_xgspxx.style.opacity="0";
    switch_splb.style.opacity="0";
    switch_sfchz.style.opacity="0";
    switch_cgrkd.style.opacity="0";
    switch_xsthrkd.style.opacity="0";
    switch_xsckd.style.opacity="0";
    switch_cgthckd.style.opacity="0";
    switch_kctbd.style.opacity="0";
    switch_kctbjl.style.opacity="1";

    sy.style.zIndex="11";
    switch_sjsp.style.zIndex="10";
    switch_xjsp.style.zIndex="9";
    switch_xgspxx.style.zIndex="8";
    switch_splb.style.zIndex="7";
    switch_sfchz.style.zIndex="6";
    switch_cgrkd.style.zIndex="5";
    switch_xsthrkd.style.zIndex="4";
    switch_xsckd.style.zIndex="3";
    switch_cgthckd.style.zIndex="2";
    switch_kctbd.style.zIndex="1";
    switch_kctbjl.style.zIndex="12";
}