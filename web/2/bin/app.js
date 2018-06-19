$(function() {
    $("body").imagesLoaded(function() {
        app = function() {
            if ($(window).width() >= 768) {
                $(".col-sm-3").width(function() {
                    return 0.25 * $(".row").width() - 30
                })
                $(".col-sm-6").width(function() {
                    return 0.5 * $(".row").width() - 30
                })
                $(".stick").stick_in_parent()
                $(".stick").on("sticky_kit:bottom", function() {
                    $(this).parent().css("position", "static");
                })
            } else {
                $(".col-sm-6, .col-sm-3").css("width", "100%")
                $(".stick").trigger("sticky_kit:detach")
            }
        }
        app()
        $(window).resize(function() {
            app()
        })
    })
})
