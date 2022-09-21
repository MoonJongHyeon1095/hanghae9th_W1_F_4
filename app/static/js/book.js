$(document).ready(function () {
    bookReview_list()

    $("#reviewbtn").click(function (){
        $("#commentshow").toggleClass("hidden");
    })

});





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