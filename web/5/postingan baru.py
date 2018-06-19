import datetime, re, os

judul = raw_input("Judul tulisan: ")

judulstrip = judul[:]
judulstrip = judulstrip.lower()
judulstrip = re.sub(r" -", r"", judulstrip)
judulstrip = re.sub(r"\(", r"", judulstrip)
judulstrip = re.sub(r"\)", r"", judulstrip)
judulstrip = re.sub(r"\"", r"", judulstrip)
judulstrip = re.sub(r"\?", r"", judulstrip)
judulstrip = re.sub(r"!", r"", judulstrip)
judulstrip = re.sub(r"\.", r"", judulstrip)
judulstrip = re.sub(r",", r"", judulstrip)
judulstrip = re.sub(r":", r"", judulstrip)
judulstrip = re.sub(r"=", r"", judulstrip)
judulstrip = re.sub(r" ", r"-", judulstrip)

judul = re.sub(r"\"", r"\"", judul)

sekarang = datetime.datetime.now()

tahun = sekarang.year
bulan = sekarang.month
tanggal = sekarang.day

if bulan < 10:
	bulan = "0" + str(bulan)
if tanggal < 10:
	tanggal = "0" + str(tanggal)

namafile = "{tahun}-{bulan}-{tanggal}-{judulstrip}.md"
isifile = """---
layout: post
title: "{judul}"
category: story
---

"""

namafile = namafile.format(
	tahun = tahun,
	bulan = bulan,
	tanggal = tanggal,
	judulstrip = judulstrip
)
isifile = isifile.format(
	judul = judul
)

buatfile = open("_posts/"+namafile, "w")
buatfile.write(isifile)

os.system("subl _posts/"+namafile)