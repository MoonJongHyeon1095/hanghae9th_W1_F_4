
/** 상세 페이지 로드시 바로 실행해야하는 함수들 넣어주세요 */
function renderBookContents() {
    bookReview_list();

    // $("#reviewbtn").click(function (){
    //     $("#commentshow").toggleClass("hidden");
    // })
}

// DEPRECATED
/** 리뷰작성 모달창 */
function reviewPostModal() {
    console.log("review modal");

    $("#section-post").load("/book/postreview", complete=activateReviewModal);
}

function activateReviewModal(responseText, textStatus, req) {
    if (textStatus == "error") {
        alert("로그인을 먼저 해주세요");
    }
    $("#modal-edit").addClass("is-active");
}

/** 리뷰 작성 제출 */
function reviewPostSubmit() {
    console.log("post review");

    data = {
        "book_id": location.search.split("id=")[1],
        "content": $("#review-content").val(),
        "star": $("#review-star").val(),
    }
    console.log(data);
    $.ajax({
        type: "POST",
        url: "/book/postreview",
        data: data,
        success: (response) => {
            // $("#modal-edit").removeClass("is-active");
            alert("리뷰를 등록했습니다");
            window.location.reload();
        },
        error: () => {
            alert("로그인을 먼저 해주세요");
        }
    });
}


/** 리뷰 삭제 */
function bookReviewDelete(review_id) {
    console.log("click")
    $.ajax({
        type: "GET",
        url: "/book/reviewdelete?review_id=" + review_id,
        data: {},
        success: (response)=>{
            switch (PATH) {
                case "/mypage/":
                    renderMypageContents()
                    break;
                case "/book/view/":
                    renderBookContents()
                    break;
            }
        },
        error: (error)=>{
            alert("작성자만 삭제할 수 있습니다.")
        }
    });
}


/** 상세페이지 책에 달린 리뷰 목록 요청 */
function bookReview_list() {
    $("#review_commnetbox").empty();
    const isbn = location.search.split("id=")[1]

    $.ajax({
        type:'GET',
        url: '/book/review',
        data: { isbn_give : isbn },
        success: function (response) {
            const reviews = response["reviews"];
            for(let i=0; i<reviews.length;i++){
                const review_id = reviews[i]["_id"];
                const username = reviews[i]["username"];
                const rating = reviews[i]["rating"];
                const time = reviews[i]["time"];
                const content = reviews[i]["content"];
                const temp_html = `<article class="media">                                             
                                        <div class="media-content" style="margin-top:-10px;">
                                            <div class="content">
                                                <p>
                                                    <strong>${username}</strong> <small>@${username}</small> <small>${time}</small>
                                                    <br>
                                                    ${content}
                                                </p>
                                            </div>
                        
                                            <nav class="level is-mobile" style="max-height: 30px;margin-bottom:-5px;">
                                                <div class="level-left">
                                                    <a class="level-item" aria-label="reply">
                                                        <span class="icon is-small">
                                                            <i class="fas fa-reply" aria-hidden="true"></i>
                                                        </span>
                                                    </a>
                                                    <a class="level-item" aria-label="retweet">
                                                        <span class="icon is-small">
                                                            <i class="fas fa-retweet" aria-hidden="true"></i>
                                                        </span>
                                                    </a>
                                                    <a class="level-item" aria-label="like">
                                                        <span class="icon is-small">
                                                        <i class="fas fa-heart" aria-hidden="true"></i>
                                                        </span>
                                                    </a>
                                                    <a class="level-item" style="margin-left:15px;margin-bottom:5px;font-size:1.3em;">
                                                        <span class="icon is-small">⭐x${rating}</span>
                                                    </a>
                                                </div>
                                            </nav>
                                            </div>
                                            <div class="media-right">
                                                <button class="delete" onclick="bookReviewDelete('${review_id}')" id="reviewDeleteButton"></button>
                                            </div>
                                        </div>
                                    </article>`;
                $("#review_commnetbox").append(temp_html);
            }
        }
    });
}

