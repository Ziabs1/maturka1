plik = open('c:/Users/Patryk/Desktop/zad 6 maturalne/dane_6_3.txt')
dane = plik.readlines()
plik.close()
for i in range(len(dane)):
    dane[i] = dane[i].replace('\n', '')
print(dane)
wyniki = open("c:/Users/Patryk/Desktop/zad 6 maturalne/wyniki6_3.txt", "w")
for i in range(len(dane)):
    wyraz, szyfr = dane[i].split(' ')
    for j in range(len(wyraz) - 1):
        new_k = (ord(szyfr[j]) - ord(wyraz[j]) + 26) % 26
        k = (ord(szyfr[j + 1]) - ord(wyraz[j + 1]) + 26) % 26
        if k != new_k:
            wyniki.write(wyraz + '\n')
            break
wyniki.close()