
plik = open('c:/Users/Patryk/Desktop/zad 6 maturalne/dane_6_1.txt')
dane = plik.readlines()
plik.close()
k = (107 % 26)
print(k)
for i in range(len(dane)):
    dane[i] = dane[i].replace('\n', '')
print(dane)
for i in range(len(dane)):
    temp =''
    for j in range(len(dane[i])):
        if (ord(dane[i][j]) + k > 90):
            temp += chr(ord(dane[i][j]) + k - 26)
        else:
            temp += chr(ord(dane[i][j]) + k)
    dane[i] = temp

print(dane)

wynik = open('c:/Users/Patryk/Desktop/zad 6 maturalne/wyniki6_1.txt',"w")
for i in range(len(dane)):
    wynik.write(dane[i]+'\n')

wynik.close()

