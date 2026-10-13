import requests
r = requests.get('https://img.sltbot.com/player/92CCUP828/battles?o=h')
Links ='''
https://img.sltbot.com/player/92CCUP828/battles?o=h
https://img.sltbot.com/player/92CCUP828/winstreaks?o=h
https://img.sltbot.com/player/92CCUP828/wsmax?o=h
https://img.sltbot.com/player/92CCUP828/powers?o=h
https://img.sltbot.com/player/92CCUP828/brawlers_legacy?o=h
https://img.sltbot.com/player/92CCUP828/trophies?o=h
https://img.sltbot.com/player/92CCUP828/trmax?o=h
https://img.sltbot.com/player/92CCUP828/ranks?o=h
https://img.sltbot.com/player/92CCUP828/ranks_50?o=h
https://img.sltbot.com/player/92CCUP828/ranks_legacy?o=h
https://img.sltbot.com/player/92CCUP828/mastery?o=h
https://img.sltbot.com/player/92CCUP828/mastery_points?o=h
'''
with open("saved_image.png", "wb") as f:
    f.write(r.content)
print(r.status_code)
