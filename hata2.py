try:
    sayi1=int(input("bir sayı giriniz."))
    sayi2=int(input("bir sayı giriniz"))
    print("sayılarınızın bölümü:",sayı1/sayi2)
except ValueError:
    print("girdiginiz deger int olmalı.")
except ZeroDivisionError:
    print("bir sayı sıfıra bolunmez")
