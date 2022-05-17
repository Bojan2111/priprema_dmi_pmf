'''
  Napisati program koji učitava dimenziju niza 1 ≤ K ≤ 50, a zatim i niz prirodnih brojeva
  manjih od 10000 zadate dimenzije K (vršiti kontrolu unosa). Potom je potrebno ispisati na
  ekranu sve elemente niza koji su delioci maksimalnog elementa niza. Npr. za K = 7 i niz
  L = [5, 18, 4, 36, 15, 9, 17], ispisuju se elementi 18, 4, 36 i 9, jer je maksimalni element
  36.
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
      maksimum = max(niz)
      print(" ".join([str(j) for j in niz if maksimum % j == 0]))
    else :
      print("Broj mora biti u rasponu od 1 do 50.")
  except ValueError:
    print("Niste uneli broj.")
  nastavak = input("Zelite li nastaviti (d/n): ")
print("Hvala sto ste koristili nas program.")
