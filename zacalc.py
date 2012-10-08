#!/usr/bin/env python
#
#       zacalc-gtk-1.3.py
#       
#       Copyright 2010 Fitra Aditya <fitra@idmail.or.id>
#		Modified (1) 2011 Ari Effendi <zerosix06@gmail.com>
#		Modified (2) 2011 Abd Azis Ws <ul2albab@gmail.com>
#       
#		Powered by BlankOn Linux Developer (2010)
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
except:  
	print("GTK Not Availible")
	sys.exit(1)

gaji1		= 0
gaji2		= 0
kebutuhan1	= 0
emas		= 0
beras		= 0

license = """BlankOn Zakat Calculator is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License(GPL v3) as published by 
the Free Software Foundation

BlankOn Zakat Calculator is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with BlankOn Zakat Calculator; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA."""

class ZaCalc(object):

	def __init__(self):
		#gtk entry
		self.entry1 = gtk.Entry()
		self.entry2 = gtk.Entry()
		self.entry3 = gtk.Entry()
		self.entry4 = gtk.Entry()
		self.entry5 = gtk.Entry()

		#gtk label
		self.out1 = gtk.Label()
		self.out2 = gtk.Label()
		self.out3 = gtk.Label()
		self.out4 = gtk.Label()
		self.out5 = gtk.Label()
		self.out6 = gtk.Label()
		self.out7 = gtk.Label()
		self.out8 = gtk.Label()
		self.out9 = gtk.Label()
		self.out10 = gtk.Label()
		self.out11 = gtk.Label()
		self.out12 = gtk.Label()

		labelA = gtk.Label('')
		labelA.set_markup('<b>PENDAPATAN</b>')
		labelB = gtk.Label('')
		labelB.set_markup('<b>ZAKAT PENGHASILAN</b>')
		labelC = gtk.Label('')
		labelC.set_markup('<b>ZAKAT SIMPANAN</b>')

		label1 = gtk.Label("Pendapatan / gaji (per bulan)")
		label2 = gtk.Label("Pendapatan lain (per bulan)")
		label3 = gtk.Label("Pendapatan total (per tahun)")
		label4 = gtk.Label("Kebutuhan (per bulan)")
		label5 = gtk.Label("Kebutuhan total (per tahun)")
		label6 = gtk.Label("Sisa pendapatan")

		label7 = gtk.Label("Harga beras saat ini (per Kg)")
		label8 = gtk.Label("Besarnya nishab")
		label9 = gtk.Label("Wajib zakat penghasilan ?")
		label10 = gtk.Label("Besarnya zakat penghasilan yang harus dibayarkan")
		label11 = gtk.Label("Zakat Per tahun")
		label12 = gtk.Label("Zakat Per bulan")

		label13 = gtk.Label("Harga emas saat ini (per gram)")
		label14 = gtk.Label("Besarnya nishab")
		label15 = gtk.Label("Wajib zakat simpanan ?")
		label16 = gtk.Label("Besarnya zakat simpanan yang harus dibayarkan")
		label17 = gtk.Label("Zakat Per tahun")
		label18 = gtk.Label("Zakat Per bulan")

		#gtk button
		button1 = gtk.Button(stock='gtk-about')
		button2 = gtk.Button("_Hitung Zakat")
		button3 = gtk.Button(stock='gtk-clear')
		button4 = gtk.Button(stock='gtk-close')

		#vbox
		vbox1 = gtk.VBox(False, 5)
		vbox2 = gtk.VBox(False, 5)

		#buttonbox
		buttonbox = gtk.HButtonBox()
		buttonbox.set_spacing(15)
		buttonbox.set_layout(gtk.BUTTONBOX_CENTER)

		buttonbox.add(button1)
		buttonbox.add(button2)
		buttonbox.add(button3)
		buttonbox.add(button4)

		#image
		pixbuf = gtk.gdk.pixbuf_new_from_file("/usr/share/zaclac/logo.png")
		image = gtk.Image()
		image.set_from_pixbuf(pixbuf)
		image.show()

		#table
		table1 = gtk.Table(1,6,True)
		table2 = gtk.Table(1,6,True)

		#frame
		frame = gtk.Frame()
		frame.set_shadow_type(gtk.SHADOW_ETCHED_IN)

		#align
		align1 = gtk.Alignment(0.5, 0.3, 0, 0)
		align2 = gtk.Alignment(0.5, 0.1, 0, 0)
		align3 = gtk.Alignment(0.5, 0.5, 0, 0)

		#layout inserting
		vbox1.add(frame)
		vbox1.add(buttonbox)

		frame.add(align1)
		align1.add(table1)
		align3.add(vbox2)
		align2.add(table2)

		table1.attach(image,3,6,0,10)

		table1.attach(labelA,0,3,0,1)

		table1.attach(label1,0,2,1,2)
		table1.attach(label2,0,2,2,3)
		table1.attach(label3,0,2,3,4)
		table1.attach(label4,0,2,4,5)
		table1.attach(label5,0,2,5,6)
		table1.attach(label6,0,2,6,7)

		table1.attach(self.entry1,2,3,1,2)
		table1.attach(self.entry2,2,3,2,3)
		table1.attach(self.out1,2,3,3,4)
		table1.attach(self.entry3,2,3,4,5)
		table1.attach(self.out2,2,3,5,6)
		table1.attach(self.out3,2,3,6,7)

		table1.attach(labelB,0,3,8,9)

		table1.attach(label7,0,2,9,10)
		table1.attach(label8,0,2,10,11)
		table1.attach(label9,0,2,11,12)
		table1.attach(label10,0,3,12,13)

		table1.attach(self.entry4,2,3,9,10)
		table1.attach(self.out4,2,3,10,11)
		table1.attach(self.out5,2,3,11,12)

		table1.attach(label11,0,2,13,14)
		table1.attach(label12,0,2,14,15)

		table1.attach(self.out6,2,3,13,14)
		table1.attach(self.out7,2,3,14,15)

		table1.attach(labelC,3,5,8,9)

		table1.attach(label13,3,5,9,10)
		table1.attach(label14,3,5,10,11)
		table1.attach(label15,3,5,11,12)
		table1.attach(label16,3,6,12,13)

		table1.attach(self.entry5,5,6,9,10)
		table1.attach(self.out8,5,6,10,11)
		table1.attach(self.out9,5,6,11,12)

		table1.attach(label17,3,5,13,14)
		table1.attach(label18,3,5,14,15)

		table1.attach(self.out10,5,6,13,14)
		table1.attach(self.out11,5,6,14,15)

		#property
		frame.set_label('')

		self.clear_value(self)

		self.out1.set_alignment(xalign=0.95, yalign=0.5)
		self.out2.set_alignment(xalign=0.95, yalign=0.5)
		self.out3.set_alignment(xalign=0.95, yalign=0.5)
		self.out4.set_alignment(xalign=0.95, yalign=0.5)
		self.out5.set_alignment(xalign=0.05, yalign=0.5)
		self.out6.set_alignment(xalign=0.95, yalign=0.5)
		self.out7.set_alignment(xalign=0.95, yalign=0.5)
		self.out8.set_alignment(xalign=0.95, yalign=0.5)
		self.out9.set_alignment(xalign=0.05, yalign=0.5)
		self.out10.set_alignment(xalign=0.95, yalign=0.5)
		self.out11.set_alignment(xalign=0.95, yalign=0.5)

		labelA.set_alignment(xalign=0, yalign=0.5)
		labelB.set_alignment(xalign=0, yalign=0.5)
		labelC.set_alignment(xalign=0, yalign=0.5)

		label1.set_alignment(xalign=0, yalign=0.5)
		label2.set_alignment(xalign=0, yalign=0.5)
		label3.set_alignment(xalign=0, yalign=0.5)
		label4.set_alignment(xalign=0, yalign=0.5)
		label5.set_alignment(xalign=0, yalign=0.5)
		label6.set_alignment(xalign=0, yalign=0.5)
		label7.set_alignment(xalign=0, yalign=0.5)
		label8.set_alignment(xalign=0, yalign=0.5)
		label9.set_alignment(xalign=0, yalign=0.5)
		label10.set_alignment(xalign=0, yalign=0.5)
		label11.set_alignment(xalign=0, yalign=0.5)
		label12.set_alignment(xalign=0, yalign=0.5)
		label13.set_alignment(xalign=0, yalign=0.5)
		label14.set_alignment(xalign=0, yalign=0.5)
		label15.set_alignment(xalign=0, yalign=0.5)
		label16.set_alignment(xalign=0, yalign=0.5)
		label17.set_alignment(xalign=-0, yalign=0.5)
		label18.set_alignment(xalign=-0, yalign=0.5)
		image.set_alignment(xalign=0, yalign=0.5)

		table1.set_col_spacings(30)			
		align1.set_padding(5, 5, 15, 15)
		table2.set_col_spacings(0)			
		align2.set_padding(0, 0, 0, 0)

		#signal
		self.entry1.connect("changed",  self.valid_number)
		self.entry2.connect("changed",  self.valid_number)
		self.entry3.connect("changed",  self.valid_number)
		self.entry4.connect("changed",  self.valid_number)
		self.entry5.connect("changed",  self.valid_number)

		button1.connect("clicked",  self.show_about)
		button2.connect("clicked",  self.calculate)
		button3.connect("clicked",  self.clear_value)
		button4.connect("clicked",  gtk.main_quit)

		icon_theme = gtk.icon_theme_get_default()
		try:
			self.icon = icon_theme.load_icon("zacalc", 48, 0)
		except Exception, e:
			print "can't load icon", e

		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_resizable(False)
		window.set_size_request(800,520) #window title
		window.set_border_width(12) #padding
		window.set_position(gtk.WIN_POS_CENTER) #default position
		window.set_title("BlankOn Zakat Calculator") #window title
		window.connect("delete_event", gtk.main_quit)
		window.connect('key_press_event', self.key_press_event)

		try:
			window.set_icon(self.icon) #icon
		except Exception, e:
			print e.message
			sys.exit(1)

		window.add(vbox1)
		window.show_all()

	def calculate(self, widget):
		gaji1 = self.get_value(self.entry1)
		gaji2 = self.get_value(self.entry2)
		total = (gaji1+gaji2) * 12
		self.out1.set_markup(self.text_show(total))

		kebutuhan1 = self.get_value(self.entry3)
		kebutuhan = kebutuhan1 * 12
		self.out2.set_markup(self.text_show(kebutuhan))

		sisa = total - kebutuhan
		self.out3.set_markup(self.text_show(sisa))

		beras = self.get_value(self.entry4)
		nishab1 = beras * 520
		self.out4.set_markup(self.text_show(nishab1))

		emas = self.get_value(self.entry5)
		nishab2 = emas * 85
		self.out8.set_markup(self.text_show(nishab2))

		if total > nishab1:
			if sisa > 0:
				self.out5.set_markup(self.text_yes())
				tahun1 = 0.025 * sisa
				tahun1 = int(tahun1)
				self.out6.set_markup(self.text_show(tahun1))

				bulan1 = tahun1 / 12
				bulan1 = int(bulan1)
				self.out7.set_markup(self.text_show(bulan1))
			else:
				self.out5.set_markup(self.text_no())
				self.out6.set_markup(self.text_zero())
				self.out7.set_markup(self.text_zero())
				tahun1 = 0

		if (sisa - tahun1) > nishab2:
			self.out9.set_markup(self.text_yes())
			tahun2 = 0.025 * ( sisa - tahun1 )
			tahun2 = int( tahun2 )
			self.out10.set_markup(self.text_show(tahun2))

			bulan2 = tahun2 / 12
			bulan2 = int( bulan2 )
			self.out11.set_markup(self.text_show(bulan2))
		else:
			self.out9.set_markup(self.text_no())
			self.out10.set_markup(self.text_zero())
			self.out11.set_markup(self.text_zero())

	def clear_value(self, widget):
		self.entry1.set_text("0")
		self.entry1.set_alignment(1)
		self.entry2.set_text("0")
		self.entry2.set_alignment(1)
		self.entry3.set_text("0")
		self.entry3.set_alignment(1)
		self.entry4.set_text("0")
		self.entry4.set_alignment(1)
		self.entry5.set_text("0")
		self.entry5.set_alignment(1)

		self.out1.set_text("0")
		self.out2.set_text("0")
		self.out3.set_text("0")
		self.out4.set_text("0")
		self.out5.set_text("-")
		self.out6.set_text("0")
		self.out7.set_text("0")
		self.out8.set_text("0")
		self.out9.set_text("-")
		self.out10.set_text("0")
		self.out11.set_text("0")

	def get_value(self, widget):
		text = widget.get_text()

		if text == "":
			widget.set_text("0")
			text = int(0)

		return int(text)

	def key_press_event(self, widget, event):
		keyname = gtk.gdk.keyval_name(event.keyval)
		if keyname == "Return":
			self.calculate(self)
		elif keyname.lower() == "c":
			self.clear_value(self)

	def show_about(self, widget):
		a=["Fitra Aditya <fitra@idmail.or.id>","Ari Effendi <zerosix06@gmail.com>","Abd Azis Ws <ul2albab@gmail.com>"]
		translate = """Alfian Fahmi <ketua@surabaya.di.blankon.in>"""
		design = ["Abd Azis Ws <ul2albab@gmail.com>"]

		about = gtk.AboutDialog()
		about.set_program_name("BlankOn Zakat Calculator")
		about.set_version("1.3")
		about.set_copyright("(c) 2011 BlankOn Linux")
		about.set_comments("BlankOn Zakat Calculator is Moslem tool to calculate the amount of zakat must be spent every year or every month")
		about.set_website("http://www.blankonlinux.or.id")
		about.set_authors(a)
		about.set_translator_credits(translate)
		about.set_artists(design)
		about.set_license(license)
		about.set_logo(self.icon)
		about.run()
		about.destroy()

	def text_show(self, value):
		return "<b>"+str(value)+"</b>"

	def text_yes(self):
		return '<span foreground="#007000" weight="Bold">Wajib Zakat</span>'

	def text_no(self):
		return '<span foreground="red" weight="Bold">Tidak Wajib</span>'

	def text_zero(self):
		return '<b>0</b>'

	#entry validation only number
	def valid_number(self, widget, *args):
		text = widget.get_text().strip()
		widget.set_text('' .join([i for i in text if i in '1234567890']))
  
if __name__ == "__main__":
	nisab = ZaCalc()
	gtk.main()