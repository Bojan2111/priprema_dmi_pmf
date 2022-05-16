'''
	Program na početku treba da učita prirodan broj N>100. Treba vršiti kontrolu unosa. Od učitanog
	broja N, treba generisati niz L na sledeći način: svaki element niza će dobiti vrednost druge cifre
	broja N, a niz će imati onoliko elemenata kolika je vrednost prve cifre broja N.
	Primer: N=24873; L=[4,4]. Treba omogućiti višestruko izvršavanje programa.
'''

def niz_druge_cifre() :
	nastavak = "d"
	while nastavak == "d" :
		broj = input("unesite prirodan broj veci od 100: ")
		try:
			if int(broj) > 100 :
				niz = []
				cifra1 = int(broj[0])
				cifra2 = int(broj[1])
				while len(niz) < cifra1 :
					niz.append(cifra2)
				print(f"Dobijeni niz je: {niz}")
				nastavak = input("Zelite li jos jednom pokrenuti program? d/n ")
			else:
				print("Niste uneli pravilan broj.")
		except ValueError:
			print("niste uneli broj.")
	print("hvala sto ste koristili nas program")

if __name__ == "__main__":
	niz_druge_cifre()