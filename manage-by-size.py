#scripts compare files by size using dict in python, and remove files with the same size. 
# size amount files is quit unique. So almost never size of two different files is not the same....
# of course they are better methods like check sum and etc. but it should be simple and easy in implementing....

import os


class MyFile:
	iloscObiektow=0
	iloscDuplikatow=0

	def __init__(self,ident):
		self.ident =  ident
		self.ilosc = 0
		self.saDuplikaty=False
		self.names = []
		self.lennames=[]
		MyFile.iloscObiektow=MyFile.iloscObiektow + 1
	def dodaj_nazwe(self,name):
		self.names.append(name)
		self.lennames.append(len(name))
		self.ilosc = self.ilosc + 1
		if self.ilosc>1:
			self.saDuplikaty=True
	def del_file_with_name(self,filename):
		print("File to remove ==========================>")
		print(filename)
		os.remove(filename)
	def wyswietl(self):
		print("===========================")
		print(self.ident)
		print(self.saDuplikaty)
		print(self.ilosc)
		print("+++++++++++++++++++++++++++")
		j=0
		for l in self.names:
			print(l)
			print(self.lennames[j])
			j=j+1
		print("+++++++++++++++++++++++++++")
		print("===========================")
	def wyswietl_do_usuw(self):
		if self.saDuplikaty:
			j=0
			dlugosc_nazwy=0
			poprzednia_dlugosc=0
			
			print("Jest cos do wykasowania")
			licznik=0
			for i in self.names:
				dlugosc_nazwy=len(i)
				if poprzednia_dlugosc == 0:
					poprzednia_dlugosc=dlugosc_nazwy
				else:
					#usuwam o najkrotszej nazwie
					if dlugosc_nazwy<poprzednia_dlugosc:
						#usuwam biezacy plik
						print("Plik do usuniecia => ")
						print("=========================>{} ",i)
						print(type(i))
						nazwa=str(i)
						self.del_file_with_name(nazwa)
					else:
						#usuwam poprzedni plik
						print("Plik do usuniecia => ")
						print("=========================>{}",self.names[licznik])
						nazwa=str(self.names[licznik])
						self.del_file_with_name(nazwa)
					#
			licznik=licznik + 1	
			#
		else:
			print("Nic nie ruszamy => brak duplikatow")
	
	def wyswietlPodsumowanieKlasy():
		print("###########################")
		print(MyFile.iloscObiektow)
		print("###########################")
	


#print(os.getcwd())

size_freq = dict()
files = (os.listdir())


for f in files:
	#print(f)
	#print(os.stat(f).st_size)
	rozmiar=os.stat(f).st_size
	if rozmiar not in size_freq:
		d = MyFile(rozmiar)
		d.dodaj_nazwe(f)
		size_freq[rozmiar] = d
	else:
		l = size_freq[rozmiar]
		l.dodaj_nazwe(f)

#print(size_freq)
#print(size_freq.values())


for k in size_freq:
	lokalny = size_freq[k]
	lokalny.wyswietl()
	lokalny.wyswietl_do_usuw()
	
MyFile.wyswietlPodsumowanieKlasy()

