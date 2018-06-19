$(function(){
	query = location.hash.substr(1);
	android = function(){
		$(".tombol").removeClass("is-active");
		$(".tombol-android").addClass("is-active");
		$(".isi").hide();
		$(".isi-android").show();
		$("title").text("Android - Zen.");	
	}
	excel = function(){
		$(".tombol").removeClass("is-active");
		$(".tombol-excel").addClass("is-active");
		$(".isi").hide();
		$(".isi-excel").show();
		$("title").text("Excel - Zen.");
	}
	python = function(){
		$(".tombol").removeClass("is-active");
		$(".tombol-python").addClass("is-active");
		$(".isi").hide();
		$(".isi-python").show();
		$("title").text("Python - Zen.");
	}
	web = function(){
		$(".tombol").removeClass("is-active");
		$(".tombol-web").addClass("is-active");
		$(".isi").hide();
		$(".isi-web").show();
		$("title").text("Web - Zen.");
	}
	android();
	$(".tombol-android").click(function(){
		android();
	});
	$(".tombol-excel").click(function(){
		excel();
	});
	$(".tombol-python").click(function(){
		python();
	});
	$(".tombol-web").click(function(){
		web();
	});
	if (query == "android"){
		android();
	} else if (query == "excel"){
		excel();
	} else if (query == "python"){
		python();
	} else if (query == "web"){
		web();
	}
});