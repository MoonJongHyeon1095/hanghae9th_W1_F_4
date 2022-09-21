


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





