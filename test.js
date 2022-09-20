


function test() {
    const id = "1231231"
    $.ajax({
        type: "GET",
        url: "/book/detail?book_id=" + id,
        data: {},
        success: (res) => {}
    })
    return
}