$(()=>{
    mypageMyReviewList();
    mypageMyLikesList();
});


/** 마이페이지 내가 작성한 리뷰 리스트 */
function mypageMyReviewList() {
    $.ajax({
        type: "GET",
        url: "/mypage/reviews",
        data: {},
        success: (response) => {
            const reviews = response.reviews;
            
            $("#my-reviews").empty();
            reviews.map( (review) => {
                const card = `
              <div class="card my-review-card">
                <div class="card-body">
                  <blockquote class="blockquote mb-0">
                    <a>${review.content}</a>
                    <footer class="blockquote-footer"><cite title="Source Title">${review.username} (${review.time})</cite></footer>
                  </blockquote>
                </div>
              </div>`;
                $("#my-reviews").append(card);
            });
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
            console.log(books)

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
                    card += `<i class="bi bi-hand-thumbs-up-fill" onclick="bookLikesToggler('${book._id}')">${book.likes.length}</i>
                    </div>
                </div>`;
                } else {
                    card += `<i class="bi bi-hand-thumbs-up" onclick="bookLikesToggler('${book._id}')">${book.likes.length}</i>
                    </div>
                </div>`;
                }
                  
                $("#my-likes").append(card);
            });
        }
    })
    return ;
}


/** 프로필 수정 창 열기 */
function mypageProfile() {
    console.log("profile modal")

    $("#section-post").load("/mypage/profile", complete=activateModal);
}

/** 프로필 모달창 is-active 클래스 부여 */
function activateModal() {
    $("#modal-edit").addClass("is-active")
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
        url: "/mypage/test",
        data: formdata,
        cache: false,
        contentType: false,
        processData: false,
        success: (response) => {
            console.log(response);
        }
    })

    return ;
}

// DEPRECATED
function getInputFileName() {
    const fileInput = document.querySelector('#file-image input[type=file]');
    fileInput.onchange = () => {
        if (fileInput.files.length > 0) {
            const fileName = document.querySelector('#file-image .file-name');
            fileName.textContent = fileInput.files[0].name;
            console.log(fileName)
        }
    }
}



/** 책 좋아요 & 해제 토글 */
function bookLikesToggler(id) {
    console.log(id)
    $.ajax({
        type: "GET",
        url: "/book/likes?book_id=" + id,
        data: {},
        success: (response) => {
            mypageMyLikesList();
        }
    })
}


