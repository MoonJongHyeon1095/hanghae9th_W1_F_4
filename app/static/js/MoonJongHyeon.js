// <!-- 로그인 페이지 (signin.html) 함수 -->

function signout() {
    $.removeCookie('mytoken', {path: '/'});
    window.location.replace("/")
}

function signinModalPop() {
    $('#section-post').load('/user/sign_in', complete=activateModal )
}

function signinSubmit() {
    const email = $("#input-email").val()
    const password = $("#input-password").val()

    if (email == "") {
        $("#help-email").text("아이디를 입력해주세요.")
        $("#input-email").focus()
        return;
    } else {
        $("#help-email").text("")
    }

    if (password == "") {
        $("#help-password").text("비밀번호를 입력해주세요.")
        $("#input-password").focus()
        return;
    } else {
        $("#help-password").text("")
    }
    $.ajax({
        type: "POST",
        url: "/user/sign_in",
        data: {
            email_give: email,
            password_give: password
        },
        success: function (response) {
            if (response['result'] == 'success') {
                $.cookie('mytoken', response['token'], {path: '/'});
                window.location.replace("/")
            } else {
                alert(response['msg'])
            }
        }
    });
}


// <!-- 회원가입 페이지(signup.html) 함수 -->

function signupSubmit() {
    const username = $('#input-username').val()
    const email = $('#input-email').val()
    const password = $('#input-password').val()
    const password2 = $('#input-password2').val()

    //0.유저네임 확인
    if (username == "") {
        $("#help-username").text("이름을 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-username").focus()
        return;
    }else{
        $("#help-username").text("사실 이름이야 아무래도 좋습니다.").removeClass("is-danger").addClass("is-success")
    }


    // 1.이메일 색깔론
    if ($("#help-email").hasClass("is-danger")) {
        alert("이메일을 다시 확인해주세요.")
        return;
    } else if (!$("#help-email").hasClass("is-success")) {
        alert("이메일 중복확인을 해주세요.")
        return;
    }

    // 2.패스워드 공백일 때
    if (password == "") {
        $("#help-password").text("비밀번호를 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-password").focus()
        return;
    } else if (!is_password(password)) {
        $("#help-password").text("비밀번호의 형식을 확인해주세요. 영문과 숫자 필수 포함, 특수문자(!@#$%^&*) 사용가능 8-20자").removeClass("is-safe").addClass("is-danger")
        $("#input-password").focus()
        return
    } else {
        $("#help-password").text("사용할 수 있는 비밀번호입니다.").removeClass("is-danger").addClass("is-success")
    }
    if (password2 == "") {
        $("#help-password2").text("비밀번호를 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-password2").focus()
        return;
    } else if (password2 != password) {
        $("#help-password2").text("비밀번호가 일치하지 않습니다.").removeClass("is-safe").addClass("is-danger")
        $("#input-password2").focus()
        return;
    } else {
        $("#help-password2").text("비밀번호가 일치합니다.").removeClass("is-danger").addClass("is-success")
    }

    $.ajax({
        type: "POST",
        url: "/user/sign_up/save",
        data: {
            email_give: email,
            password_give: password,
            username_give: username
        },
        success: function (response) {
            alert("회원가입 성공!")
            window.location.replace("/")
        }
    });
}

function is_email(asValue) {
    const regExp = /^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
    return regExp.test(asValue);
}

function is_password(asValue) {
    const regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/;
    return regExp.test(asValue);
}

function check_dup() {
    const email = $("#input-email").val()
    console.log(email)

    // 1.공백일 때
    if (email == "") {
        $("#help-email").text("이메일을 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-email").addClass("is-danger").focus()
        return;
    }

    // 2.정규표현식 검사
    if (!is_email(email)) {
        $("#help-email").text("올바른 이메일 형식이 아닙니다.").removeClass("is-safe").addClass("is-danger")
        $("#input-email").addClass("is-danger").focus()
        return;
    }

    // 3.위 1,2번 통과시
    $("#input-email").removeClass("is-danger")
    $("#help-email").removeClass("is-danger").addClass("is-loading")
    $.ajax({
        type: "POST",
        url: "/user/check_dup",
        data: {
            email_give: email
        },
        success: function (response) {

            if (response["exists"]) {
                $("#help-email").text("이미 가입된 이메일입니다.").removeClass("is-safe").addClass("is-danger")
                $("#input-email").addClass("is-danger").focus()
            } else {
                $("#help-email").text("사용할 수 있는 이메일입니다.").removeClass("is-danger").addClass("is-success")
                $("#input-email").removeClass("is-danger").addClass("is-success").focus()
            }
            $("#help-email").removeClass("is-loading")
        }
    });
}
