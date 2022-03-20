import random
while True:
    seviye=input("bir seviye seciniz(kolay, orta, zor):"). upper() #lower:sayıyı kücüge cevir. upper:büyüğe cevirir.
    print(seviye)
    if seviye=="kolay":
        uret=random.randint(1,10) #bir ile on arasında rastgele sayı üretir.
    elif seviye=="orta":
        uret=random.randint(1,50)
    elif seviye=="zor":
        uret=random.randint(1,100)
    else:
        print("lütfen dogru giris yapınız")
while True:
    tahmin=int(input("tahmininiz:"))
    if tahmin==uret:
         print("tebrikler, sayıyı buldunuz")
         break
    elif tahmin<uret:
        print("üzgünüm, daha büyük bir sayı giriniz.")
    else:
        print("üzgünüm sayıyı kücültün.")