jQuery(function($) {
    $.getJSON('http://public-api.wordpress.com/rest/v1/sites/en.blog.wordpress.com/posts/?number=1&callback=?')
        .success(function(response) {
            var $content = $('#content')
                .html(response.posts[0].content);

            $content.find('img').each(function() {
                var $this = $(this);
                $this.height($this.height() / 2);
                $this.width($this.width() / 2);
            });

            $('#title')
                .html(response.posts[0].title)
                .attr('href', response.posts[0].URL);
        });
});