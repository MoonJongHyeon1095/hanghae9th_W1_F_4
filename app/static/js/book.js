$(document).ready(function () {
    bookReview_list()

    $("#reviewbtn").click(function (){
        $("#commentshow").toggleClass("hidden");
    })

});

function reviewPostModal() {
    console.log("review modal")

    $("#section-post").load("/book/postreview", complete=activateModal2)
}

function activateModal2(responseText, textStatus, req) {
    if (textStatus == "error") {
        alert("로그인을 먼저 해주세요")
    }
    $("#modal-edit").addClass("is-active")
}

function reviewPostSubmit() {
    console.log("post review")

    data = {
        "book_id": location.search.split("id=")[1],
        "content": $("#review-content").val(),
        "star": $("#review-star").val(),
    }
    $.ajax({
        type: "POST",
        url: "/book/postreview",
        data: data,
        success: (response) => {
            $("#modal-edit").removeClass("is-active");
            alert("리뷰를 등록했습니다");
            window.location.reload();
        },
        error: () => {
            alert("로그인을 먼저 해주세요")
        }
    })
}

function bookReview_list() {
    $.ajax({
        type: 'GET',
        url: '/book/review',
        data: {},
        success: function (response) {
            let reviews = response["reviews"]
            for(let i=0; i<reviews.length;i++){
                let username = reviews[i]["username"]
                let rating = reviews[i]["rating"]
                let time = reviews[i]["time"]
                let content = reviews[i]["content"]
                let temp_html = `<article class="media">
                                            <figure class="media-left">
                                                <p class="image is-64x64">
                                                  <img src="https://bulma.io/images/placeholders/128x128.png">
                                                </p>
                                              </figure>
                                                        
                                        <div class="media-content">
                                            <div class="content">
                                                <p>
                                                    <strong>${username}</strong> <small>@${username}</small> <small>${time}</small>
                                                    <br>
                                                    ${content}
                                                </p>
                                            </div>
                        
                                            <nav class="level is-mobile">
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
                                                </div>
                                            </nav>
                                            </div>
                                          <div class="media-right">
                                            <button class="delete"></button>
                                          </div>
                                        </div>
                                    </article>`
                $("#review_commnetbox").append(temp_html)
            }

        }
    })
}
