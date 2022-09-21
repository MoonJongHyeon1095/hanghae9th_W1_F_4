


$(document).ready(function () {

    console.log(location.pathname)

})





// function bookSearch_list() {
//     $(".tile.is-ancestor").empty()
//     $.ajax({
//         type: "GET",
//         url: "/book/list/",
//         data: {},
//         success: function (response) {
//             console.log(response)
//             let booklist = response["books"]
//             for (let i = 0; i < booklist.length; i++) {
//                 let author = booklist[i]["author"]
//                 let image = booklist[i]["image"]
//                 let title = booklist[i]["title"]
//                 let pubdate = booklist[i]["pubdate"]
//                 let publisher = booklist[i]["publisher"]
//                 let discount = booklist[i]["discount"]
//                 let description = booklist[i]["description"]

//                 let temp_html = `<div class="tile is-4">
//                                             <div class="tile is-parent">
//                                                 <article class="tile is-child notification">
//                                                     <figure class="image">
//                                                         <img class="is-rounded"
//                                                              src="${image}">
//                                                     </figure>
//                                                 </article>
//                                             </div>
//                                         </div>

//                                         <div class="tile is-parent">
//                                             <article class="tile is-child notification ">
//                                                 <div class="book_content">
//                                                     <p class="title">${title}</p>
//                                                     <p class="subtitle">${author}</p>
//                                                     <hr>
//                                                     <div class="content">
//                                                         <p>${pubdate}</p>
//                                                         <p>${publisher}</p>
//                                                         <p>${discount}</p>
//                                                         <p>${description}</p>
//                                                     </div>
//                                                     <div class="buttons">
//                                                         <button class="button is-primary is-light">Review</button>
//                                                     </div>
//                                                 </div>
//                                             </article>
//                                         </div>`
//                 $(".tile.is-ancestor").append(temp_html)
//             }
//         }
//     })
// }





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
