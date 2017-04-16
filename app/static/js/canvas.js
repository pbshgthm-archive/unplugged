console.log("this script works");
var article_id = "{{ article_id }}";

var getData = function()
{
    $.ajax({
        url: "http://127.0.0.1:8000/canvas/secret",
        data: { "article_id" : article_id },
        type: 'GET',
        dataType: "JSON",
        contentType: "multipart/form-data",
        success: function(response){console.log(response)}  
    });
}

window.onload = function()
{
    // $('#title').html("{{article.title}}");
    // $('#content').html("{{article.content}}");
    // $('#picture_location').html("{{article.picture_location}}");
    console.log("this script runs");
    getData();
    //document.getElementById("done").onclick = send_data;
    };