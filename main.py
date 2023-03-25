import requests
import time
from playsound import playsound

# Instagram hesabının kullanıcı adı
username = 'kullaniciadi'

# Başlangıç takipçi sayısı
previous_followers = 0

while True:
    # Instagram hesabının takipçi sayısını kontrol edin
    response = requests.get(f'https://www.instagram.com/{username}/?__a=1')
    data = response.json()
    current_followers = int(data['graphql']['user']['edge_followed_by']['count'])

    # Takipçi sayısındaki değişimi kontrol edin
    follower_diff = current_followers - previous_followers
    if follower_diff > 0:
        # Yeni bir takipçi geldiğinde bir ses çıkartın
        playsound('path/to/sound.mp3')

    # Önceki takipçi sayısını güncelleyin
    previous_followers = current_followers

    # 1 dakika bekle
    time.sleep(60)
