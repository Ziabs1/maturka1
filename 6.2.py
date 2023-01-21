
plik = open('c:/Users/Patryk/Desktop/zad 6 maturalne/dane_6_2.txt')
dane = plik.readlines()
plik.close()
for i in range(len(dane)):
    dane[i] = dane[i].replace('\n', '')
print(dane)

for i in range(len(dane)):
    temp =''
    tab=dane[i].split(' ')
    if tab[1] == "":
        continue
    k = int(tab[1]) % 26
    for j in range(len(tab[0])):
        if (ord(tab[0][j]) - k < 65):
            temp += chr(ord(tab[0][j]) - k + 26)
        else:
            temp += chr(ord(tab[0][j]) - k)
    dane[i] = temp
print(dane)


wynik = open('c:/Users/Patryk/Desktop/zad 6 maturalne/wyniki6_2.txt',"w")
for i in range(len(dane)):
    wynik.write(dane[i]+'\n')
wynik.close()
