#!/usr/bin/env python
#
#       zacalc-gtk.py
#       
#       Copyright 2010 Fitra Aditya <fitra@idmail.or.id>
#		Modified 2011 Ari Effendi <zerosix06@gmail.com>
#       
#       BlankOn Zakat Calculator is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License (GPL v3) as published by
#       the Free Software Foundation.
#       
#       BlankOn Zakat Calculator is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with BlankOn Zakat Calculator; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

try:  
	import pygtk  
	pygtk.require("2.0")  
except:  
	pass  
try:  
	import gtk  
	import gtk.glade  
except:  
	print("GTK Not Availible")
	sys.exit(1)

class ZaCalc(object):
	gaji1 = 0
	gaji2 = 0
	kebutuhan1 = 0
	emas = 0
	beras = 0
	
	def __init__(self):
		self.gladefile = "glade/zacalc.glade"
		self.wTree = gtk.glade.XML(self.gladefile)
		dic = {
			"on_button1_clicked" : self.show_about,
			"on_button2_clicked" : self.HitungZakat,
			"on_button3_clicked" : gtk.main_quit,
			"on_button4_clicked" : self.Clear,
			
			"on_entry1_changed" : self.Validasi,
			"on_entry2_changed" : self.Validasi,
			"on_entry3_changed" : self.Validasi,
			"on_entry4_changed" : self.Validasi,
			"on_entry5_changed" : self.Validasi,
			}
		self.wTree.signal_autoconnect(dic)
		self.window = self.wTree.get_widget("ZaCalc")
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.connect('key_press_event', self.on_key_press_event)
		self.window.show()
		
	def Ambil(self,entry):
		teks = self.wTree.get_widget(entry)
		nilai = teks.get_text()
		
		if nilai == "":
			teks.set_text("0")
			nilai = int(0)
		
		return int(nilai)
	
	def Tampil(self,entry,value):
		self.wTree.get_widget(entry).set_markup("<b>"+str(value)+"</b>")
	
	def Ya(self,entry):
		self.wTree.get_widget(entry).set_markup('<span foreground="#00cc00" weight="bold">Ya</span>')
	
	def Tidak(self,entry):
		self.wTree.get_widget(entry).set_markup('<span foreground="red" weight="bold">Tidak</span>')
	
	def Nol(self,entry):
		self.wTree.get_widget(entry).set_markup('<b>0</b>')

	
	def Total(self):
		gaji1 = self.Ambil("entry1")
		gaji2 = self.Ambil("entry2")
		total = (gaji1 + gaji2) * 12
		self.Tampil("lbl1",total)
		
		kebutuhan1 = self.Ambil("entry3")
		kebutuhan = kebutuhan1 * 12
		self.Tampil("lbl2",kebutuhan)
		
		sisa = total - kebutuhan
		self.Tampil("lbl3",sisa)
		
		beras = self.Ambil("entry4")
		nishab1 = beras * 520
		self.Tampil("lbl4",nishab1)
		
		emas = self.Ambil("entry5")
		nishab2 = emas * 85
		self.Tampil("lbl8",nishab2)
		
		if total > nishab1:
			if sisa > 0:
				self.Ya("lbl5")
				tahun1 = 0.025 * sisa
				tahun1 = int(tahun1)
				self.Tampil("lbl6",tahun1)
				
				bulan1 = tahun1 / 12
				bulan1 = int( bulan1 )
				self.Tampil("lbl7",bulan1)
			else:
				self.Tidak("lbl5")
				self.Nol("lbl6")
				self.Nol("lbl7")
				tahun1 = 0
		
		if (sisa - tahun1) > nishab2:
			self.Ya("lbl9")
			tahun2 = 0.025 * ( sisa - tahun1 )
			tahun2 = int( tahun2 )
			self.Tampil("lbl10",tahun2)
			
			bulan2 = tahun2 / 12
			bulan2 = int( bulan2 )
			self.Tampil("lbl10",bulan2)
		else:
			self.Tidak("lbl9")
			self.Nol("lbl10")
			self.Nol("lbl11")

	
	#validasi hanya angka
	def Validasi(self,widget,*args):
		text = widget.get_text().strip()
		widget.set_text(''.join([i for i in text if i in '0123456789']))
			
	def HitungZakat(self,widget):
		self.Total()
		
	def show_about(self,widget):
		self.wTree.get_widget("window_about").run()
		self.wTree.get_widget("window_about").hide()
	
	def Clear(self):
		self.wTree.get_widget("entry1").set_text("0")
		self.wTree.get_widget("entry2").set_text("0")
		self.wTree.get_widget("entry3").set_text("0")
		self.wTree.get_widget("entry4").set_text("0")
		self.wTree.get_widget("entry5").set_text("0")
		
		self.wTree.get_widget("lbl1").set_text("")
		self.wTree.get_widget("lbl2").set_text("")
		self.wTree.get_widget("lbl3").set_text("")
		self.wTree.get_widget("lbl4").set_text("")
		self.wTree.get_widget("lbl5").set_text("")
		self.wTree.get_widget("lbl6").set_text("")
		self.wTree.get_widget("lbl7").set_text("")
		self.wTree.get_widget("lbl8").set_text("")
		self.wTree.get_widget("lbl9").set_text("")
		self.wTree.get_widget("lbl10").set_text("")
		self.wTree.get_widget("lbl11").set_text("")

	def on_key_press_event(self, widget, event):
		keyname = gtk.gdk.keyval_name(event.keyval)
		if keyname == "Return":
			self.Total()
		elif keyname.lower() == "c":
			self.Clear()
		
if __name__ == "__main__":	
	nisab = ZaCalc()
	gtk.main()
