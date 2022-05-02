function bindCaptchaBtnClick() {
    $("#captcha-btn").on("click", function (event) {
        var email = $("input[name='email']").val();
        var $this = $(this);
        if (!email) {
            alert("请先输入邮箱!");
            return;
        }
        $.ajax({
            url: "/user/captcha",
            method: "POST",
            data: {
                "email": email
            },
            success: function (res) {
                var code = res['code'];
                if(code == 200){
                    //取消点击事件
                    $this.off("click");
                    //开始倒计时
                    var countdown = 60;
                    var timer = setInterval(function () {
                        if (countdown > 0){
                              $this.text(countdown+"秒后重新发送");
                        }else{
                            $this.text("获取验证码");
                            //重新执行下这个函数 重新绑定点击事件
                            bindCaptchaBtnClick();
                            clearInterval(timer);
                        }
                        countdown -= 1;
                    }, 1000);
                    alert("验证码发送成功!");
                }else{
                    alert(res['message']);
                }
            }
        })
    });
}

//等待网页文档所有元素加载完成之后再执行
$(function () {
    bindCaptchaBtnClick();
});