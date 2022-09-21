
$(document).ready(function () {
    book_list()
})


function book_list() {
    $.ajax({

        type: 'GET',
        url: '/book/list',
        data: {},
        success: function (response) {

            let lists = response["books"]
            for(let i=0; i< lists.length;i++){
                let image = lists[i]['image']
                let title = lists[i]['title']
                let author = lists[i]['author']
                let isbn = lists[i]["isbn"]

                let temp_html = `<div class="tile is-parent">
                                    <article class="tile is-child box">
                                        <a href="/book/view?book_id=${isbn}"><img src="${image}"></a>
                                        <p class="title">${title}</p>
                                        <p class="subtitle">${author}</p>
                                    </article>
                                    </div>
                                <div>`
                $("#list_review").append(temp_html)
            }
        }
    });
}

