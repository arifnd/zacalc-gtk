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
		
		label1 = gtk.Label("Pendapatan / gaji (per bulan)")
		label2 = gtk.Label("Pendapatan lain-lain (per bulan)")
		label3 = gtk.Label("Pendapatan total (per tahun)")
		label4 = gtk.Label("Kebutuhan (per bulan)")
		label5 = gtk.Label("Kebutuhan total (per tahun)")
		label6 = gtk.Label("Sisa pendapatan")
		
		label7 = gtk.Label("Harga beras saat ini (per Kg)")
		label8 = gtk.Label("Besarnya nishab")
		label9 = gtk.Label("Wajib zakat penghasilan?")
		label10 = gtk.Label("Besarnya zakat penghasilan yang harus dibayarkan")
		label11 = gtk.Label("Per tahun")
		label12 = gtk.Label("Per bulan")
		
		label13 = gtk.Label("Harga emas saat ini (per gram)")
		label14 = gtk.Label("Besarnya nishab")
		label15 = gtk.Label("Wajib zakat simpanan?")
		label16 = gtk.Label("Besarnya zakat simpanan yang harus dibayarkan")
		label17 = gtk.Label("Per tahun")
		label18 = gtk.Label("Per bulan")
		
		#gtk button
		button1 = gtk.Button(stock='gtk-about')
		button2 = gtk.Button("_Hitung Zakat")
		button3 = gtk.Button(stock='gtk-clear')
		button4 = gtk.Button(stock='gtk-close')
		
		#vbox
		vbox1 = gtk.VBox(False, 5)
		vbox2 = gtk.VBox(False, 5)
		vbox3 = gtk.VBox(False, 5)
		
		#buttonbox
		buttonbox = gtk.HButtonBox()
		
		#table
		table1 = gtk.Table(6,2,True)
		table2 = gtk.Table(3,2,True)
		table3 = gtk.Table(2,2,True)
		table4 = gtk.Table(3,2,True)
		table5 = gtk.Table(2,2,True)
		
		#frame
		frame1 = gtk.Frame()
		frame2 = gtk.Frame()
		
		#align
		align1 = gtk.Alignment(0.5, 0.5, 0, 0)
		align2 = gtk.Alignment(0.5, 0.5, 0, 0)
		
		#layout inserting
		vbox1.add(table1)
		vbox1.add(frame1)
		vbox1.add(frame2)
		vbox1.add(buttonbox)
		
		vbox2.add(table2)
		vbox2.add(label10)
		vbox2.add(table3)
		
		vbox3.add(table4)
		vbox3.add(label16)
		vbox3.add(table5)
		
		frame1.add(align1)
		frame2.add(align2)
		
		align1.add(vbox2)
		align2.add(vbox3)
		
		table1.attach(label1,0,1,0,1)
		table1.attach(label2,0,1,1,2)
		table1.attach(label3,0,1,2,3)
		table1.attach(label4,0,1,3,4)
		table1.attach(label5,0,1,4,5)
		table1.attach(label6,0,1,5,6)
		table1.attach(self.entry1,1,2,0,1)
		table1.attach(self.entry2,1,2,1,2)
		table1.attach(self.out1,1,2,2,3)
		table1.attach(self.entry3,1,2,3,4)
		table1.attach(self.out2,1,2,4,5)
		table1.attach(self.out3,1,2,5,6)
		
		table2.attach(label7,0,1,0,1)
		table2.attach(label8,0,1,1,2)
		table2.attach(label9,0,1,2,3)
		table2.attach(self.entry4,1,2,0,1)
		table2.attach(self.out4,1,2,1,2)
		table2.attach(self.out5,1,2,2,3)
		
		table3.attach(label11,0,1,0,1)
		table3.attach(label12,0,1,1,2)
		table3.attach(self.out6,1,2,0,1)
		table3.attach(self.out7,1,2,1,2)
		
		table4.attach(label13,0,1,0,1)
		table4.attach(label14,0,1,1,2)
		table4.attach(label15,0,1,2,3)
		table4.attach(self.entry5,1,2,0,1)
		table4.attach(self.out8,1,2,1,2)
		table4.attach(self.out9,1,2,2,3)
		
		table5.attach(label17,0,1,0,1)
		table5.attach(label18,0,1,1,2)
		table5.attach(self.out10,1,2,0,1)
		table5.attach(self.out11,1,2,1,2)
		
		buttonbox.add(button1)
		buttonbox.add(button2)
		buttonbox.add(button3)
		buttonbox.add(button4)
		
		#property
		frame1.set_label("ZAKAT PENGHASILAN")
		frame2.set_label("ZAKAT SIMPANAN")
		
		self.clear_value(self)
		
		self.out1.set_alignment(xalign=0, yalign=0.5)
		self.out2.set_alignment(xalign=0, yalign=0.5)
		self.out3.set_alignment(xalign=0, yalign=0.5)
		self.out4.set_alignment(xalign=0, yalign=0.5)
		self.out5.set_alignment(xalign=0, yalign=0.5)
		self.out6.set_alignment(xalign=0, yalign=0.5)
		self.out7.set_alignment(xalign=0, yalign=0.5)
		self.out8.set_alignment(xalign=0, yalign=0.5)
		self.out9.set_alignment(xalign=0, yalign=0.5)
		self.out10.set_alignment(xalign=0, yalign=0.5)
		self.out11.set_alignment(xalign=0, yalign=0.5)
		
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
		label16.set_alignment(xalign=-0, yalign=0.5)
		label17.set_alignment(xalign=-0, yalign=0.5)
		label18.set_alignment(xalign=-0, yalign=0.5)
		
		table1.set_col_spacings(30)
		table2.set_col_spacings(35)
		table3.set_col_spacings(35)
		table3.set_row_spacings(10)
		table4.set_col_spacings(35)
		table5.set_col_spacings(35)
		table5.set_row_spacings(10)
		
		align1.set_padding(0, 10, 10, 10)
		align2.set_padding(0, 10, 10, 10)
		
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
			self.icon = icon_theme.load_icon("accessories-calculator", 48, 0)
		except Exception, e:
			print "can't load icon", e
		
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_resizable(False)
		window.set_size_request(410,530) #window title
		window.set_border_width(10) #padding
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
		self.entry2.set_text("0")
		self.entry3.set_text("0")
		self.entry4.set_text("0")
		self.entry5.set_text("0")

		self.out1.set_text("")
		self.out2.set_text("")
		self.out3.set_text("")
		self.out4.set_text("")
		self.out5.set_text("")
		self.out6.set_text("")
		self.out7.set_text("")
		self.out8.set_text("")
		self.out9.set_text("")
		self.out10.set_text("")
		self.out11.set_text("")

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
		a=["Fitra Aditya <fitra@idmail.or.id>","Ari Effendi <zerosix06@gmail.com>"]

		about = gtk.AboutDialog()
		about.set_program_name("BlankOn Zakat Calculator")
		about.set_version("1.2")
		about.set_copyright("(c) 2011 BlankOn Linux")
		about.set_comments("BlankOn Zakat Calculator is tool to calculate the amount of zakat must be spent every year or every month")
		about.set_website("http://www.blankonlinux.or.id")
		about.set_authors(a)
		about.set_license(license)
		about.set_logo(self.icon)
		about.run()
		about.destroy()

	def text_show(self, value):
		return "<b>"+str(value)+"</b>"

	def text_yes(self):
		return '<span foreground="#00cc00" weight="bold">Ya</span>'

	def text_no(self):
		return '<span foreground="red" weight="bold">Tidak</span>'

	def text_zero(self):
		return '<b>0</b>'

	#entry validation only number
	def valid_number(self, widget, *args):
		text = widget.get_text().strip()
		widget.set_text(''.join([i for i in text if i in '0123456789']))

if __name__ == "__main__":
	nisab = ZaCalc()
	gtk.main()
