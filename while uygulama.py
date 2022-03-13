# kullanıcı adı ve şifre alınız. kullanıcı adı olarak "admin" şifre olarak
# 123456 girilince
#  "sisteme başarıyla giriş yaptınız yazsın" :
# yanlış girilince "kullanıcı adı veya şifre hatalı" desin
# tekrar kullanıcı adı ve şifre sorsun
while True:
        kullanıcıadı=input("kullanıcı adı giriniz:")
        sifre=input("parolanız:")
        if kullanıcıadı=="admin" and sifre=="123456":
           break
        else:
           print("kullanıcı adı veya parola hatali.")