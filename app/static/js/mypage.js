


/** mypage.html 로드되고 나서 바로 실행해야하는 함수 여기에 넣어주세요. */
function renderMypageContents() {
    mypageMyReviewList();
    mypageMyLikesList();
}


/** 마이페이지 내가 작성한 리뷰 리스트 */
function mypageMyReviewList() {
    $.ajax({
        type: "GET",
        url: "/mypage/reviews",
        data: {},
        success: ({ reviews }) => {
            
            if(reviews.length !== 0) {
                $("#my-reviews").empty();
                reviews.map( (review) => {
                    const card = `
                <div class="card my-review-card">
                    <div class="card-body">
                    <blockquote class="blockquote mb-0">
                        <a>${review.content}</a>
                        <div class="footers">
                            <button class="delete" onclick="bookReviewDelete('${review._id}')" id="reviewDeleteButton"></button>
                            <footer class="blockquote-footer"><cite title="Source Title">${review.username} (${review.time})</cite></footer>
                        </div>
                    </blockquote>
                    </div>
                </div>`;
                    $("#my-reviews").append(card);
                });
            } else if(reviews.length === 0) {
                $("#my-reviews").empty();
                const card = `<h1>작성한 리뷰가 없습니다</h1>`
                $("#my-reviews").append(card);
            }
        }
    });
    return ;
}


/** 마이페이지 내가 좋아요를 누른 영화 리스트 */
function mypageMyLikesList() {
    $.ajax({
        type: "GET",
        url: "/mypage/likes",
        data: {},
        success: ({ books }) => {

            if(books.length !== 0) {
                $("#my-likes").empty();
                books.map( (book) => {
                    let card = `            <div class="card my-likes-card" style="width: 18rem;">
                    <img src=${book.image} class="card-img-top" alt="...">
                    <div class="card-body">
                    <h5 class="card-title">${book.title}</h5>
                    <a class="card-author">${book.author}</a>
                    <div class="card-publish">
                        <a class="card-publisher">${book.publisher}</a>
                        <a class="card-pubdate">${book.pubdate}</a>
                    </div>`
                    if (book.flag) {
                        card += `<i class="bi bi-hand-thumbs-up-fill" onclick="bookLikesToggler('${book._id}', ${book.flag})">${book.likes.length}</i>
                        </div>
                    </div>`;
                    } else {
                        card += `<i class="bi bi-hand-thumbs-up" onclick="bookLikesToggler('${book._id}', ${book.flag})">${book.likes.length}</i>
                        </div>
                    </div>`;
                    }
                    
                    $("#my-likes").append(card);
                });
            } else if(books.length === 0) {
                $("#my-likes").empty();
                const card = `<h1>좋아하는 책에 <i class="bi bi-hand-thumbs-up" style="color:rgba(255, 95, 95, 0.781)"></i>를 눌러주세요.</h1>`
                $("#my-likes").append(card);
            }

            
        }
    })
    return ;
}



/** 프로필 수정 창 열기 */
function mypageProfile() {
    console.log("profile modal")

    $("#section-post").load("/mypage/profile", complete=activateModal);

    // $("#section-post").load("/mypage/profile", (responseText, textStatus, req)=>{
    //     if (textStatus === "success") $("#modal-pop").addClass("is-active")
    // });
}


/** 프로필 수정 요청 */
function mypageProfileUpdate() {
    console.log("update profile")
    const username = $("#input-username").val();
    const password = $("#input-password").val();
    const password2 = $("#input-password2").val();
    const image = $("#input-image")[0].files[0];

    // console.log(username, password, image)
    let formdata = new FormData();
    formdata.append("username", username)
    formdata.append("password", password)
    formdata.append("password", password2)
    formdata.append("image", image);

    for (const key of formdata.entries()) {
        console.log(key[0] + ', ' + key[1]);
    }

    $.ajax({
        type: "POST",
        url: "/mypage/profile",
        data: formdata,
        cache: false,
        contentType: false,
        processData: false,
        success: ({ msg, mytoken }) => {
            console.log(msg);
            $.cookie("mytoken", mytoken, {path: "/"});
            $("#modal-edit").removeClass("is-active")
            alert(msg)
            location.reload();
        }
    });
}


/** 책 좋아요 & 해제 토글 */
function bookLikesToggler(id, flag) {
    console.log(id)
    $.ajax({
        type: "GET",
        url: `/book/likes?book_id=${id}&flag=${flag}`,
        data: {},
        success: () => {
            switch (PATH) {  
                case "/mypage/":
                    renderMypageContents()
                    break;
                case "/book/view/":
                    location.reload()
                    break;
            }
        },
        error: ()=>{
            alert("로그인을 먼저 해주세요.")
        }
    });
}


// DEPRECATED
function getInputFileName() {
    const fileInput = document.querySelector('#file-image input[type=file]');
    fileInput.onchange = () => {
        if (fileInput.files.length > 0) {
            const fileName = document.querySelector('#file-image .file-name');
            fileName.textContent = fileInput.files[0].name;
            console.log(fileName);
        }
    }
}


// DEPRECATED
function navToMypage() {
    $.ajax({
        type: "GET",
        url: "/mypage/nav",
        data: {},
        success: (response) => {
            console.log("success")
        }
    });
}
