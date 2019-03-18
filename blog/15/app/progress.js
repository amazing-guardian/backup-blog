---
---

bahasa = []
{% for x in site.posts %}
	{% if x.bahasa %}
		bahasa.push('{{ x.bahasa }}')
	{% endif %}
{% endfor %}

function grup_frekuensi(arr) {
    var a = [], b = [], prev;

    arr.sort();
    for ( var i = 0; i < arr.length; i++ ) {
        if ( arr[i] !== prev ) {
            a.push(arr[i]);
            b.push(1);
        } else {
            b[b.length-1]++;
        }
        prev = arr[i];
    }

    return [a, b];
}

bahasa_grup = grup_frekuensi(bahasa)

bahasa_grup_2 = []
for (n in bahasa_grup[0]){
	bahasa_grup_2.push([0, 0])
	bahasa_grup_2[n][0] = bahasa_grup[0][n]
	bahasa_grup_2[n][1] = bahasa_grup[1][n]
}

function compareSecondColumn(a, b) {
	return a[1] - b[1]
}

bahasa_grup_2.sort(compareSecondColumn).reverse()

frekuensi_tertinggi_pemrograman = 0
for (n in bahasa_grup[1]){
	if (bahasa_grup[1][n] > frekuensi_tertinggi_pemrograman){
		frekuensi_tertinggi_pemrograman = bahasa_grup[1][n]
	}
}

for (n in bahasa_grup_2){
	progress = ''
	persen = bahasa_grup_2[n][1] * 100 / frekuensi_tertinggi_pemrograman
	progress += '<div data-progress="' + persen + '" class="row induk_progress">'
		progress += '<div class="col-xs-3">'
			progress += bahasa_grup_2[n][0]
		progress += '</div>'
		progress += '<div class="col-xs-9">'
			progress += '<div class="progress">'
				progress += '<div class="progress-bar" style="width: ' + persen + '%;">'
			progress += '</div>'
		progress += '</div>'
	progress += '</div>'
	$('tbody.pemrograman').append(progress)
}

list_progress = []
$('.induk_progress').each(function(){
	list_progress.push($(this).attr('data-progress'))
})

// $('.induk_progress').slideUp()
for (n = 1; n <= 5; n++){
	$('.induk_progress:nth-child('+ n +')').show()
}