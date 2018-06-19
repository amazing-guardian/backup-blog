// acak

function shuffle(array) {
    var currentIndex = array.length,
        temporaryValue, randomIndex;

    // While there remain elements to shuffle...
    while (0 !== currentIndex) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}

posts = shuffle(posts)
posts2 = []
for (n = 0; n < posts.length; n++) {
    if (posts[n].kategori == kategori) {
        posts2.push(posts[n])
    }
}

// menampilkan related posts

$target = $(".row .col-sm-4")

for (n = 0; n < posts2.length; n++) {
    $target.eq(n).find("a").attr("href", posts2[n].link)
    $target.eq(n).find("img").attr("src", posts2[n].gambar)
    $target.eq(n).find("p").text(posts2[n].judul)
}
