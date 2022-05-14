def trougao() :

	def povrsina_trougla(koord) :
		x1 = koord[0][0]
		y1 = koord[0][1]
		x2 = koord[1][0]
		y2 = koord[1][1]
		x3 = koord[2][0]
		y3 = koord[2][1]
		return (abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))/2

	def kombinacije(lst, n):
		if n == 0:
			return [[]]
		l =[]
		for i in range(0, len(lst)):
			m = lst[i]
			remLst = lst[i + 1:]
			for p in kombinacije(remLst, n-1):
				l.append([m]+p)
		return l

	dimenzija = int(input("Unesite broj tacaka u koordinatnom sistemu: (3 <= n <= 1000) "))
	niz = []
	brojac = 1
	while len(niz) < dimenzija :
		xosa = int(input(f"Unesite vrednost x za {brojac}. tacku: "))
		yosa = int(input(f"Unesite vrednost y za {brojac}. tacku: "))
		niz.append([xosa, yosa])
		brojac += 1
	brojac = 0
	kombo = kombinacije(niz, 3)
	trg_koord_niz = []
	trg_pov_niz = []
	for i in kombo :
		trg_koord_niz.append(i)
		trg_pov_niz.append(povrsina_trougla(i))
		brojac += 1

	maks_pov = max(trg_pov_niz)
	maks_koord = trg_koord_niz[trg_pov_niz.index(max(trg_pov_niz))]
	print(f"Maksimalna povrsina: {maks_pov}\nkoordinate: A({maks_koord[0][0]}, {maks_koord[0][1]}), B({maks_koord[1][0]}, {maks_koord[1][1]}), C({maks_koord[2][0]}, {maks_koord[2][1]})")


if __name__ == '__main__':
	trougao()