#!/usr/bin/env python
#
#       zacalc.py
#       
#       Copyright 2010 Fitra Aditya <fitra@idmail.or.id>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from Tkinter import *

from tkMessageBox import *

class ZaCalc( Frame ):
	""" Tampilan Antar Muka Kalkulator Zakat """
	gaji1 = 0
	gaji2 = 0
	kebutuhan1 = 0
	emas = 0
	beras = 0
	
	def __init__( self ):
		Frame.__init__( self )
		
		self.pack( expand = YES, fill = BOTH )
		self.master.title( "Kalkulator Zakat BlankOn" )
		self.master.rowconfigure( 0, weight = 1 )
		self.master.columnconfigure( 0, weight = 1 )
		self.grid( sticky = W+N )
		
		self.Label1 = Label( self, text = "Pendapatan / Gaji (per bulan)" )
		self.Label1.grid( row = 1, column = 1, sticky = W+N, padx = 12, pady = 10 )
		
		self.Text1 = Entry( self, name = "gaji1", width = 12 )
		self.Text1.insert( INSERT, 0 )
		self.Text1.grid( row = 1, column = 2, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label2 = Label( self, text = "Pendapatan Lain-lain (per bulan)" )
		self.Label2.grid( row = 2, column = 1, sticky = W+N, padx = 12, pady = 10 )
		
		self.Text2 = Entry( self, name = "gaji2", width = 12 )
		self.Text2.insert( INSERT, 0 )
		self.Text2.grid( row = 2, column = 2, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label3 = Label( self, text = "Pendapatan Total (per tahun)" )
		self.Label3.grid( row = 3, column = 1, sticky = W+N, padx = 12, pady = 10 )
		
		self.Text3 = Label( self )
		self.Text3.grid( row = 3, column = 2, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label4 = Label( self, text = "Kebutuhan (per bulan)" )
		self.Label4.grid( row = 4, column = 1, sticky = W+N, padx = 12, pady = 10 )
		
		self.Text4 = Entry( self, name = "kebutuhan1", width = 12 )
		self.Text4.insert( INSERT, 0 )
		self.Text4.grid( row = 4, column = 2, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label5 = Label( self, text = "Kebutuhan Total (per tahun)" )
		self.Label5.grid( row = 5, column = 1, sticky = W+N, padx = 12, pady = 10 )
		
		self.Text5 = Label( self )
		self.Text5.grid( row = 5, column = 2, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label6 = Label( self, text = "Sisa Pendapatan" )
		self.Label6.grid( row = 6, column = 1, sticky = W+N, padx = 12, pady = 10 )
		
		self.Text6 = Label( self )
		self.Text6.grid( row = 6, column = 2, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label7 = Label( self, text = "ZAKAT PENGHASILAN" )
		self.Label7.grid( row = 1, column = 3, columnspan = 2, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label8 = Label( self, text = "Harga Beras Saat Ini (per kg)" )
		self.Label8.grid( row = 2, column = 3, sticky = W+N, padx = 10, pady = 10 )
		
		self.Text8 = Entry( self, name = "beras", width = 15 )
		self.Text8.insert( INSERT, 0 )
		self.Text8.grid( row = 2, column = 4, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label9 = Label( self, text = "Besarnya Nishab" )
		self.Label9.grid( row = 3, column = 3, sticky = W+N, padx = 10, pady = 10 )
		
		self.Text9 = Label( self )
		self.Text9.grid( row = 3, column = 4, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label10 = Label( self, text = "Wajib Zakat Penghasilan?" )
		self.Label10.grid( row = 4, column = 3, sticky = W+N, padx = 10, pady = 10 )
		
		self.Text10 = Label( self )
		self.Text10.grid( row = 4, column = 4, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label11 = Label( self, text = "Besarnya Zakat Penghasilan Yang Harus Dibayarkan" )
		self.Label11.grid( row = 5, column = 3, columnspan = 2, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label12 = Label( self, text = "Per Tahun" )
		self.Label12.grid( row = 6, column = 3, sticky = W+N, padx = 10, pady = 10 )
		
		self.Text12 = Label( self )
		self.Text12.grid( row = 6, column = 4, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label13 = Label( self, text = "Per Bulan" )
		self.Label13.grid( row = 7, column = 3, sticky = W+N, padx = 10, pady = 10 )
		
		self.Text13 = Label( self )
		self.Text13.grid( row = 7, column = 4, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label14 = Label( self, text = "ZAKAT SIMPANAN" )
		self.Label14.grid( row = 1, column = 5, columnspan = 2, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label15 = Label( self, text = "Harga Emas Saat Ini (per gram)" )
		self.Label15.grid( row = 2, column = 5, sticky = W+N, padx = 10, pady = 10 )
		
		self.Text15 = Entry( self, name = "emas", width = 12 )
		self.Text15.insert( INSERT, 0 )
		self.Text15.grid( row = 2, column = 6, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label16 = Label( self, text = "Besarnya Nishab" )
		self.Label16.grid( row = 3, column = 5, sticky = W+N, padx = 10, pady = 10 )
		
		self.Text16 = Label( self )
		self.Text16.grid( row = 3, column = 6, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label17 = Label( self, text = "Wajib Zakat Simpanan?" )
		self.Label17.grid( row = 4, column = 5, sticky = W+N, padx = 10, pady = 10 )
		
		self.Text17 = Label( self )
		self.Text17.grid( row = 4, column = 6, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label18 = Label( self, text = "Besarnya Zakat Simpanan Yang Harus Dibayarkan" )
		self.Label18.grid( row = 5, column = 5, columnspan = 2, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label19 = Label( self, text = "Per Tahun" )
		self.Label19.grid( row = 6, column = 5, sticky = W+N, padx = 10, pady = 10 )
		
		self.Text19 = Label( self )
		self.Text19.grid( row = 6, column = 6, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label20 = Label( self, text = "Per Bulan" )
		self.Label20.grid( row = 7, column = 5, sticky = W+N, padx = 10, pady = 10 )
		
		self.Text20 = Label( self )
		self.Text20.grid( row = 7, column = 6, sticky = W+N, padx = 10, pady = 10 )
		
		self.Label21 = Label( self, text = " " )
		self.Label21.grid( row = 8, column = 1, columnspan = 6, sticky = W+N, padx = 10, pady = 10 )
		
		self.Button22 = Button( self, text = "Hitung Zakat", command = self.HitungZakat )
		self.Button22.bind( "<Enter>", self.rolloverEnter )
		self.Button22.bind( "<Leave>", self.rolloverLeave )
		self.Button22.grid( row = 9, column = 6, sticky = W+N, padx = 10, pady = 10 )
		
	
	def Ambil1( self ):
		gaji1 = self.Text1.get()
		gaji1 = int( gaji1 )
		return gaji1
		
	def Ambil2( self ):
		gaji2 = self.Text2.get()
		gaji2 = int( gaji2 )
		return gaji2
	
	def Ambil3( self ):
		kebutuhan1 = self.Text4.get()
		kebutuhan1 = int( kebutuhan1 )
		return kebutuhan1
		
	def Ambil4( self ):
		beras = self.Text8.get()
		beras = int( beras )
		return beras
		
	def Ambil5( self ):
		emas = self.Text15.get()
		emas = int( emas )
		return emas
	
	def Total( self ):
		gaji1 = self.Ambil1()
		gaji2 = self.Ambil2()
		total = (gaji1 * 12) + (gaji2 * 12)
		self.Text3.config( text = total )
		kebutuhan1 = self.Ambil3()
		kebutuhan = kebutuhan1 * 12
		self.Text5.config( text = kebutuhan )
		sisa = total - kebutuhan
		self.Text6.config( text = sisa )
		beras = self.Ambil4()
		nishab1 = beras * 520
		self.Text9.config( text = nishab1 )
		emas = self.Ambil5()
		nishab2 = emas * 85
		self.Text16.config( text = nishab2 )
		if total > nishab1:
			if sisa > 0:
				self.Text10.config( text = "Ya" )
				tahun1 = 0.025 * sisa
				tahun1 = int( tahun1 )
				bulan1 = tahun1 / 12
				bulan1 = int( bulan1 )
				self.Text12.config( text = tahun1 )
				self.Text13.config( text = bulan1 )
			else:
				self.Text10.config( text = "Tidak" )
				self.Text12.config( text = 0 )
				self.Text13.config( text = 0 )
				tahun1 = 0
		if ( sisa - tahun1 ) > nishab2:
			self.Text17.config( text = "Ya" )
			tahun2 = 0.025 * ( sisa - tahun1 )
			tahun2 = int( tahun2 )
			self.Text19.config( text = tahun2 )
			bulan2 = tahun2 / 12
			bulan2 = int( bulan2 )
			self.Text20.config( text = bulan2 )
		else:
			self.Text17.config( text = "Tidak" )
			self.Text19.config( text = 0 )
			self.Text20.config( text = 0 )
		
	
	def HitungZakat( self ):
		self.Total()
	
	def rolloverEnter( self, event ):
   		event.widget.config( relief = GROOVE )
	
	def rolloverLeave( self, event ):
   		event.widget.config( relief = RAISED )


def main():
	ZaCalc().mainloop()

if __name__ == '__main__':
	main()
