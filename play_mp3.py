# -*- coding: utf-8 -*-

import vlc
import time



instance = vlc.Instance()

media = instance.media_new('input/mp3/start.wav')

player = instance.media_player_new()
player.set_media(media)

media.parse_with_options(1,0)

while True:
    if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
        break
    
print(media.get_duration())

player.play()

'''
duration = player.get_length()
print(duration)
'''

'''

p = vlc.MediaPlayer('input/mp3/start.wav')

duration = p.get_length()
print(duration)

p.play()

duration = p.get_length()
print(duration)

time.sleep(1)

duration = p.get_length()
print(duration)

time.sleep(1)

duration = p.get_length()
print(duration)

time.sleep(1)

duration = p.get_length()
print(duration)

'''