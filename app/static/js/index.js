const PATH = document.location.pathname;

/** 모달창 is-active 클래스 부여 */
function activateModal() {
    console.log("!!!")
    $("#modal-pop").addClass("is-active")
}

$(document).ready(function () {
    switch (PATH) {
        case "/":
            renderIndexContents();
            break;    
        case "/mypage/":
            renderMypageContents()
            break;
        case "/book/view/":
            renderBookContents()
            break;
    }
});

/** index.html 로드되고 나서 바로 실행해야하는 함수 여기에 넣어주세요. */
function renderIndexContents() {
        indexBookList();
}

function indexBookList() {
    $.ajax({
        type: 'GET',
        url: '/list',
        data: {},
        success: function (response) {
            let lists = response["b_list"];
            for (let i = 0; i < lists.length; i++) {
                let image = lists[i]['image'];
                let title = lists[i]['title'];
                let author = lists[i]['author'];
                let isbn = lists[i]["isbn"];

                let temp_html = `<div class="tile is-parent">
                                    <article class="tile is-child box">
                                        <a href="/book/view?book_id=${isbn}"><img src="${image}"></a>
                                        <p class="title">${title}</p>
                                        <p class="subtitle">${author}</p>
                                    </article>
                                    </div>
                                <div>`;
                $("#list_review").append(temp_html);
            }
        }
    });
}



