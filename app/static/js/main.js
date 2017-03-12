$(document).ready(function () {
        $("#run").click(function (e) {
            e.preventDefault();
            var target = $("#target").val();
            $.ajax ({
                url: "/pipeline",
                type: "POST",
                data: JSON.stringify({
                    target: target
                }),
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                success: function(response){
                    $.each(response, function (i, s) {
                        $("#results").append("<div>" + s  + "</div>")
                    });
                }
            });
        });
    }
);