'''
  Napisati program koji učitava dimenziju niza 1≤K≤50, a zatim i niz prirodnih brojeva manjih od
  10000 zadate dimenzije K (vršiti kontrolu unosa). Potom je potrebno ispisati na ekranu sve
  elemente niza kojima je prva cifra jednaka sa poslednjom.
  NAPOMENA: za jednocifrene elemente niza važi da je prva cifra jednaka poslednjoj.
'''

nastavak = "d"
while nastavak == "d" :
  try:
    dimenzija = int(input("Unesite dimenziju niza (1-50): "))
    niz = []
    rez = []
    if dimenzija >=1 and dimenzija <= 50 :
      brojac = 1
      while len(niz) < dimenzija :
        element = input(f"Unesite {brojac}. element niza (1-10000): ")
        try:          
          if int(element) >= 1 and int(element) <= 10000 :
            niz.append(element)
            brojac += 1
          else :
            print("Broj mora biti u rasponu od 1 do 10000.")
        except ValueError:
          print("Niste uneli broj.")
      for i in niz :
        res = ""
        if int(i[0] == i[-1]) :
          rez.append(i)
      print(f"Elementi niza cija je prva cifra jednaka poslednjoj su: {', '.join(rez)}")
    else :
      print("Broj mora biti u rasponu od 1 do 50.")
  except ValueError:
    print("Niste uneli broj.")
  nastavak = input("Zelite li nastaviti (d/n): ")
print("Hvala sto ste koristili nas program.")
