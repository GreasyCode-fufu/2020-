    //    轮播
       var wrap = document.querySelector(".wrap");
        var next = document.querySelector(".arrow_right");
        var prev = document.querySelector(".arrow_left");
        next.onclick = function () {
            next_pic();
        }
        prev.onclick = function () {
            prev_pic();
        }
        
        function next_pic () {
            var newLeft = parseInt(wrap.style.left)-600;
            wrap.style.left = newLeft + "px";
        }
        function prev_pic () {
            var newLeft = parseInt(wrap.style.left)+600;
            wrap.style.left = newLeft + "px";
        }
        function next_pic () {
            var newLeft;
            if(wrap.style.left === "-3600px"){
                newLeft = -1200;
            }else{
                newLeft = parseInt(wrap.style.left)-600;
            }
            wrap.style.left = newLeft + "px";
        }
        function prev_pic () {
            var newLeft;
            if(wrap.style.left === "0px"){
                newLeft = -2400;
            }else{
                newLeft = parseInt(wrap.style.left)+600;
            }
            wrap.style.left = newLeft + "px";
        }
        // 不同规格不同价格实现同时选中
        function myFunction1(){
            var x=document.getElementById("value");
            x.innerHTML="价格&nbsp;&nbsp;RMB&nbsp;7,799.00";
            btn1.style.boxShadow="0 0 2px 2px #bbbbbb";
            btn3.style.boxShadow="0 0 2px 2px #ffffff";
            btn2.style.boxShadow="0 0 2px 2px #ffffff";
        }
        function myFunction2(){
            var y=document.getElementById("value");
            y.innerHTML="价格&nbsp;&nbsp;RMB&nbsp;8,849.00";
            btn2.style.boxShadow="0 0 2px 2px #bbbbbb";
            btn3.style.boxShadow="0 0 2px 2px #ffffff";
            btn1.style.boxShadow="0 0 2px 2px #ffffff";
        }
        function myFunction3(){
            var z=document.getElementById("value");
            z.innerHTML="价格&nbsp;&nbsp;RMB&nbsp;7,599.00";
            btn3.style.boxShadow="0 0 2px 2px #bbbbbb";
            btn1.style.boxShadow="0 0 2px 2px #ffffff";
            btn2.style.boxShadow="0 0 2px 2px #ffffff";
        }
        function myFunction4(){
            color.style.boxShadow="0 0 2px 2px #bbbbbb";
        }
        
        //点亮心
        function changeImage(){
            element=document.getElementById('myimage')
            if(element.src.match("myimage"))
            {
                element.src="./img/xin.jpg";
            }
            else{
                element.src="./img/红心.jpg";
            }
            
        }
        //购买
        



        
       