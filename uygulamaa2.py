#kendisine gönderilen kullanıcı adı ve şifreyi
# kontrol ederek sonucunda True ya da False gönderen fonksiyon pyhton kodu
# kullanıcıadı: admin, şifre:123456 olmalı.
def kontrol(kullaniciadi,sifre):
        if kullaniciadi=="admin" and sifre=="123456":
           return True
        else:
           return False
kullaniciadi=input("kullanici adiniz:")
sifre=input("sifreniz:")
sonuc=kontrol(kullaniciadi,sifre)