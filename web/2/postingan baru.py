import datetime, re, os, random

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
judulstrip = re.sub(r" ", r"-", judulstrip)

judul = re.sub(r"\"", r"\"", judul)

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

namafile = "{tahun}-{bulan}-{tanggal}-{judulstrip}.md"
isifile = """---
layout: post
title: "{judul}"
date: {tahun}-{bulan}-{tanggal} {jam}:{menit}:{detik}
gambar: ""
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
	judulstrip = judulstrip
)

buatfile = open("_posts/"+namafile, "w")
buatfile.write(isifile)

os.system("subl _posts/"+namafile)