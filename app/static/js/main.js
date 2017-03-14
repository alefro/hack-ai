$(document).ready(function () {

        $("#run").click(function (e) {
            e.preventDefault();
            var target = $("#target").val();
            $("#results").empty();
            var spinner = new Spinner({position: "relative", top: "20px"}).spin($("#results")[0]);

            $.ajax ({
                url: "/pipeline",
                type: "POST",
                data: JSON.stringify({
                    target: target
                }),
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                success: function(response){
                    spinner.stop();

                    $.each(response, function (i, s) {
                        $("#results").append("<div>" + s.smiles  + "</div><img src=\"/img/" + s.id + ".png\">")
                    });
                }
            });
        });
    }
);