print('''1 - Toplama
2 - Çıkarma
3 - Çarpma
4 - Bölme
5 - Çıkış''')

sayi1 = int(input('1. sayıyı giriniz: '))
sayi2 = int(input('2. sayıyı giriniz: '))

secim = int(input('Seçiminizi yapın: '))

if secim == 1:
    toplama = sayi1 + sayi2
    print('Toplama işleminin sonucu:', toplama)
elif secim == 2:
    cikarma = sayi1 - sayi2
    print('Çıkarma işleminin sonucu:', cikarma)
elif secim == 3:
    carpma = sayi1 * sayi2
    print('Çarpma işleminin sonucu:', carpma)
elif secim == 4:
    bolme = sayi1 / sayi2
    print('Bölme işleminin sonucu:', bolme)
elif secim == 5:
    print('Çıkış yapılıyor...')
else:
    print('Geçersiz seçim! Lütfen tekrar deneyin.')
