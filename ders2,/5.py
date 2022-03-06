#KARŞILAŞTIRMA OPERATÖRLERİ
"""""

<  : kücüktür
>  : büyüktür
<= : kücük esit
>= : büyük esit
== : esittir
!= : esit degildir
"""
cinsiyet=input("Bir harf giriniz.")

if cinsiyet=="e" or cinsiyet=="E":
    print("cinsiyet olarak erkek giriniz.")
    print("if icinden selamlar")

elif cinsiyet=="k" or cinsiyet=="K":
    print("cinsiyet olarak kadın giriniz.")
    print("suan elif icinden selamlar.")
else:
    print("ben sana e ya da k cizerim")
    print("suanda if dısındasınız.")