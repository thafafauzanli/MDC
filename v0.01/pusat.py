"""
	Nama Project : MDC (Mudah dan Cepat)
	Platfrom : Linux
	Pengarang : Thafa Fauzanli
	Deskripsi : MDC adalah perangkat lunak yang dibuat untuk
				memudahkan pengerjaan tugas kuliah
	Versi : 0.01
	Tgl mulai : 17 Maret 2022
	Tgl selesai : -
"""

# impor modul takut kena kritik
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from docx import Document
from docx.shared import Inches
import platform
import webbrowser
import time
import random
import math

# impor fitur
from berkas_mdc.fitur.distfre import AplDistFre

# Variabel Umum Aplikasi
NAMA_APLIKASI = "MDC v0.01"
MENUJU = ""
apl = None
jalur_ikon = "berkas_mdc/gambar/ti.png"

def cek_tujuan(t):
	if t == "Distribusi Frekuensi":
		apl = None
		apl = AplDistFre(NAMA_APLIKASI, AplMenu, apl, jalur_ikon)
		apl.connect("destroy", Gtk.main_quit)
		apl.show_all()
		Gtk.main()
		MENUJU = ""
	else:
		print("tidak ada tujuan, aplikasi keluar")

class AplMenu(Gtk.Window):
	def __init__(self):
		self.judul = NAMA_APLIKASI
		self.lebar = 500
		self.tinggi = 300
		super().__init__(title=self.judul)
		self.set_icon_from_file(jalur_ikon)
		self.set_default_size(self.lebar, self.tinggi)
		self.set_resizable(False)
		self.pembuatan()
	
	def pembuatan(self):
		# kisi
		self.kisi = Gtk.Fixed()
		self.add(self.kisi)
		# logo
		self.logo = Gtk.Image()
		self.logo.set_from_file("berkas_mdc/gambar/mdc.png")
		self.kisi.put(self.logo, 100, 20)
		self.lPilih = Gtk.Label()
		self.lPilih.set_text("Pilih fitur :")
		self.kisi.put(self.lPilih, 130, 155)
		# versi
		self.versi = Gtk.Label()
		self.versi.set_label("versi 0.01")
		self.kisi.put(self.versi, 220, 120)
		# daftar pilihan
		self.daftar_fitur = ["Distribusi Frekuensi"]
		self.pilihan = Gtk.ComboBoxText()
		self.pilihan.set_entry_text_column(0)
		self.pilihan.connect("changed", self.milih_momen)
		for c in self.daftar_fitur:
			self.pilihan.append_text(c)
		self.pilihan.set_active(0)
		self.kisi.put(self.pilihan, 220, 150 )
		# tombol lanjut
		self.lanjut = Gtk.Button()
		self.lanjut.set_label("Lanjut")
		self.lanjut.connect("clicked", self.lanjut_momen)
		self.kisi.put(self.lanjut, 225, 200)
		# Pencipta
		self.pGambar = Gtk.Image()
		self.pGambar.set_from_file("berkas_mdc/gambar/ti_kecil.png")
		self.pencipta = Gtk.Button()
		self.pencipta.connect("clicked", self.pencipta_momen)
		self.pencipta.set_image(self.pGambar)
		self.kisi.put(self.pencipta, 10, 200)
	
	# Fungsi
	def milih_momen(self, combo):
		self.pohon = combo.get_active_iter()
		if self.pohon is not None:
			self.model = combo.get_model()
			self.terpilih = self.model[self.pohon][0]
			
	
	def pencipta_momen(self, button):
		webbrowser.open('http://takuni-infinity.blogspot.com')
		
	def lanjut_momen(self, button):
		global MENUJU
		global cek_tujuan
		MENUJU = self.terpilih
		self.close()
		time.sleep(1)
		cek_tujuan(MENUJU)

apl = AplMenu()
apl.connect("destroy", Gtk.main_quit)
apl.show_all()
Gtk.main()



# Debugging
print("Aplikasi berjalan lancar boss\nInformasi alat tempur:")
print("Sistem Operasi : ", platform.platform())
print("Versi : ", platform.version())
print("Nilai bit : ", platform.machine())
