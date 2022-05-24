'''
    Napisati program koji učitava dimenziju niza 1≤K≤50, a zatim i niz prirodnih brojeva manjih od
    10000 zadate dimenzije K (vršiti kontrolu unosa). Potom je potrebno ispisati na ekranu sve
    elemente niza čiji je zbir cifara dvocifren broj.
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
        res = 0
        for j in i :
          res += int(j)
        if res >= 10 and res < 100 :
          rez.append(i)
      print(f"Elementi niza ciji je zbir cifara dvocifren broj su: {', '.join(rez)}")
    else :
      print("Broj mora biti u rasponu od 1 do 50.")
  except ValueError:
    print("Niste uneli broj.")
  nastavak = input("Zelite li nastaviti (d/n): ")
print("Hvala sto ste koristili nas program.")
