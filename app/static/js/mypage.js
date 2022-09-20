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
    console.log("profile update")

    $("#section-post").load("/mypage/profile", complete=activateModal);
}

function activateModal() {
    $("#modal-edit").addClass("is-active")
}


/** 프로필 수정 요청 */
function mypageProfileUpdate() {
    const username = $("#input-username").val();
    const password = $("#input-password").val();
    const password2 = $("#input-password2").val();
    const image = $("#input-pic")[0].files[0];

    return ;
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


