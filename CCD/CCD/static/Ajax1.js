        $(function() {

          $.ajax({
            type: "POST",
            url: "/portal/search/",
            data: {
                'search_text' : "",
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });

    $('#search').keyup(function() {

        $.ajax({
            type: "POST",
            url: "/portal/search/",
            
            data: {
                'search_text' : $('#search1').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{   
    // let lis = document.getElementById("mainlist");
    // console.log(sres.childNodes.length    )
        // lis.style.display = "none";

    $('#search-results1').html(data)
}