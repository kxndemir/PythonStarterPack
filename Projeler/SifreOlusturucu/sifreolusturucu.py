import random

uzunluk = int(input('Kaç haneden oluşmasını istiyorsunuz? [Önerilen en az 8-12 karakterdir.] '))
kucuk = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
buyuk = ['A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J','K','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z']
sayi = ['0','1','2','3','4','5','6','7','8','9']
sembol = ['!','@','#','$','%','&','*','?']

sonuc = kucuk + buyuk + sayi + sembol
ran = random.sample(sonuc,uzunluk)
sifre = "".join(ran)
print(sifre)
