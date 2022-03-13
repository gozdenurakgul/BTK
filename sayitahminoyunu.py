tuttugumsayi=5
while True:
    sayi=int(input("bir sayı giriniz:"))
    if sayi<tuttugumsayi:
        print("bilemediniz.sayıyı büyütün!")
    elif sayi>tuttugumsayi:
        print("bilemediniz.sayıyı kücültün!")
    else:
        print("dogru bildiniz.")
    break
