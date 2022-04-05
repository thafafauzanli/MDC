"""
	Nama Project : MDC (Mudah dan Cepat)
	Platfrom : Linux, Windows
	Penulis : Thafa Fauzanli
	Deskripsi : MDC adalah perangkat lunak yang dibuat untuk
				memudahkan pengerjaan tugas kuliah
	Versi : 0.01re
	Tgl mulai : 02 April 2022
	Tgl selesai : -
"""

# impor paket
import PySimpleGUI as sg
from docx import Document
from docx.shared import Inches
import webbrowser
import random
import math
from os.path import exists

# impor fitur tapi takut di kritik
from berkas_mdc.fitur.distfre import AplDistFre

# Tema
tema = "Default"; apl = None; keruang = ""
sg.theme(tema)

def ganti_ruang(ruang, rm, e):
	if rm != None and e != None: apl = ruang(rm, e)
	else: apl = ruang()
	
	

# Aplikasi
class Apl(sg.Window):
	def __init__(self):
		self.judul = "MDC v0.01re"
		fitur =["Distribusi Frekuensi"]
		menu_def=[["&Menu", ["&Tentang", "&Tema"]]]
		layout = [[sg.Image("berkas_mdc/gambar/mdc.png", pad=((3,0),0))], # 1
				[sg.Text("versi 0.01re")], # 2
				[sg.Text("Fitur : "), sg.Combo(values=fitur, size=(20, 3), key="_fitur", enable_events=True, readonly=True)], # 3
				[sg.Button("Lanjut", key="_lanjut")], # 4
				[sg.Button("Tentang", key="_ti"),
					sg.Button("Tema", key="_tema")]]
		super().__init__(self.judul, layout, text_justification="c", element_justification="c", icon="berkas_mdc/gambar/ti.png")
		self.ulang()
	def ulang(self):
		global tema, apl, keruang
		while True:
			event, values = self.read()
			if event in (sg.WIN_CLOSED, 'Exit'):
				break
			if event in ("_lanjut"):
				if keruang == "Distribusi Frekuensi":
					self.close(); keruang=""; ganti_ruang(AplDistFre, Apl, ganti_ruang);
				else:
					sg.popup("Fitur nya dipilih dulu coy", icon="berkas_mdc/gambar/ti.png")
			if event in ("_fitur"):
				keruang = values[event]
			if event in ("_menu"):
				print("Menu terpilih = ", values[event])
			if event in ("_ti"):
				webbrowser.open("http://takuni-infinity.blogspot.com")
			if event in ("_tema"): 
				if tema == "Dark": tema = "Default"; sg.theme(tema)
				else: tema = "Dark"; sg.theme(tema)
				sg.change_look_and_feel(tema)
				sg.popup("Tema diubah menjadi "+tema, icon="berkas_mdc/gambar/ti.png")
				self.close(); apl = Apl(); apl.ulang()

apl = Apl()
