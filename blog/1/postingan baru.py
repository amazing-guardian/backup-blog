import datetime, re, os, random

judul = raw_input("Judul tulisan: ")

judulstrip = judul[:]
judulstrip = judulstrip.lower()
judulstrip = re.sub(r"-", r"", judulstrip)
judulstrip = re.sub(r"\(", r"", judulstrip)
judulstrip = re.sub(r"\)", r"", judulstrip)
judulstrip = re.sub(r"\?", r"", judulstrip)
judulstrip = re.sub(r"!", r"", judulstrip)
judulstrip = re.sub(r"\.", r"", judulstrip)
judulstrip = re.sub(r",", r"", judulstrip)
judulstrip = re.sub(r":", r"", judulstrip)
judulstrip = re.sub(r" ", r"-", judulstrip)

sekarang = datetime.datetime.now()

tahun = sekarang.year
bulan = sekarang.month
tanggal = sekarang.day
jam = sekarang.hour
menit = sekarang.minute
detik = sekarang.second

if bulan < 10:
	bulan = "0" + str(bulan)
if tanggal < 10:
	tanggal = "0" + str(tanggal)
if jam < 10:
	jam = "0" + str(jam)
if menit < 10:
	menit = "0" + str(menit)
if detik < 10:
	detik = "0" + str(detik)

gambar = """
http://img04.deviantart.net/d79d/i/2011/121/9/d/cats_life_by_apofiss-d3fb1qw.jpg
http://img09.deviantart.net/1b98/i/2010/240/4/5/bad_cat_by_wolf_minori-d2xg0ji.jpg
http://img07.deviantart.net/26e0/i/2013/109/f/e/just_smile_by_leejun35-d629j5x.jpg
http://img01.deviantart.net/384a/i/2010/037/8/2/converse_smile_by_choifreako.jpg
http://img09.deviantart.net/9f4c/i/2013/021/7/c/don__t_feel_blue____by_janneo-d38by92.jpg
http://img08.deviantart.net/1190/i/2012/030/e/4/if_you_feel_like_letting_go____by_nostalgicchills-d4o6rmv.jpg
http://pre12.deviantart.net/29f8/th/pre/i/2009/037/f/b/i_feel_you____young_jedi_wp_by_osokin.jpg
http://img00.deviantart.net/658f/i/2009/267/3/1/music_is_my_life_2_by_lietingadiena.jpg
http://orig08.deviantart.net/0694/f/2014/027/9/5/95266da5c023d1fc76ce2e0dc55bed9c-d73xftm.png
http://img12.deviantart.net/1b57/i/2013/266/5/5/look_for_the_bare_necessities_of_life_by_ineedchemicalx-d6nhvy1.jpg
http://t09.deviantart.net/-OkoNJH0hMw9SvPVWZBZqNAOdVk=/fit-in/700x350/filters:fixed_height%28100,100%29:origin%28%29/pre01/4563/th/pre/i/2014/048/1/4/colourful_life_by_davinsky-d6dcre0.jpg
http://img07.deviantart.net/4654/i/2016/039/2/4/key_of_life_by_kryseis_art-d9r0v1f.jpg
http://orig06.deviantart.net/95ee/f/2013/028/8/4/coming_to_life_by_aoao2-d5t0tuk.jpg
"""

gambar = gambar.splitlines()
gambar = filter(None, gambar)
gambar = random.choice(gambar)

namafile = "{tahun}-{bulan}-{tanggal}-{judulstrip}.md"
isifile = """---
layout: post
title: "{judul}"
date: {tahun}-{bulan}-{tanggal} {jam}:{menit}:{detik}
gambar: "{gambar}"
# /blog/{tahun}/{bulan}/{tanggal}/{judulstrip}.html
---

"""

namafile = namafile.format(
	tahun = tahun,
	bulan = bulan,
	tanggal = tanggal,
	judulstrip = judulstrip
)
isifile = isifile.format(
	judul = judul,
	tahun = tahun,
	bulan = bulan,
	tanggal = tanggal,
	jam = jam,
	menit = menit,
	detik = detik,
	judulstrip = judulstrip,
	gambar = gambar
)

buatfile = open("_posts/"+namafile, "w")
buatfile.write(isifile)

os.system("subl _posts/"+namafile)