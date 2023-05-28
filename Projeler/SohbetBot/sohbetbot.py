import random

cevaplar = [
    'Evet.',
    'Hayır.',
    'Bilmiyorum.',
    'Olabilir.',
    'Belki.',
    'Büyük ihtimalle.',
    'Kesinlikle.',
    'Muhtemelen.',
    'Kesinlikle hayır.',
    'Şüpheliyim.',
    'Buna emin değilim.',
    'Muhtemelen evet.',
    'Her ihtimale karşı hayır.',
    'İhtimal vermiyorum.',
    'Olası bir senaryo.',
    'Biraz daha düşünmem gerekiyor.',
    'Tahmin etmek zor.',
    'Bence öyle.',
    'Kuşkulu gözüküyor.',
    'Bu sorunun cevabını bilemiyorum.',
    'Olabilir, ama emin değilim.',
    'İmkansız değil.',
    'Daha fazla bilgi gerekiyor.',
    'Sana katılıyorum.',
    'Farklı bir açıdan bakmak gerekebilir.',
    'Bu konuda uzman değilim.',
    'Sonuçları beklemek en iyisi.',
    'Geleceği bilemiyorum.',
    'Daha sonra tekrar sor.',
    'Belirsizlikler var.',
]

while True:
    soru = input('[KULLANICI] Soru: ')
    cevap = random.choice(cevaplar)
    print('[BOT] Cevap:', cevap)
