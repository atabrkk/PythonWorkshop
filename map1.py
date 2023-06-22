# 21.06.23
# Kullanıcının girdiği üsse göre listedeki sayıların üssünün hesaplanıp yeni bir listeye aktarılması.
# map ve lambda fonksiyon kullanıldı.

numbers = [1, 15, 6, 7, 2, 3, 8, 10, -5, 4]
power = int(input("Kuvvet giriniz: "))

powersList = list(map(lambda num: pow(num, power), numbers))
print(powersList)

