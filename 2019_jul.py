'''
  Napisati program koji ucitava dimenziju niza 1 ≤ K ≤ 50, a zatim i niz prirodnih
  brojeva manjih od 10000 zadate dimenzije K (vrsiti kontrolu unosa). Potom je
  potrebno pronaci i ispisati na ekranu tri najmanja razlicita elementa niza
'''
nastavak = "d"
while nastavak == "d" :
  try:
    dimenzija = int(input("Unesite dimenziju niza (1-50): "))
    niz = []
    if dimenzija >=1 and dimenzija <= 50 :
      brojac = 1
      while len(niz) < dimenzija :
        try:
          element = int(input(f"Unesite {brojac}. element niza (1-10000): "))
          if element >= 1 and element <= 10000 :
            niz.append(element)
            brojac += 1
          else :
            print("Broj mora biti u rasponu od 1 do 10000.")
        except ValueError:
          print("Niste uneli broj.")
      sortiran_niz = sorted(niz)
      tri_najmanja = sortiran_niz[:3]
      print(" ".join([str(j) for j in tri_najmanja]))
    else :
      print("Broj mora biti u rasponu od 1 do 50.")
  except ValueError:
    print("Niste uneli broj.")
  nastavak = input("Zelite li nastaviti (d/n): ")
print("Hvala sto ste koristili nas program.")
