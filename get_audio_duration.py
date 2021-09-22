# -*- coding: utf-8 -*-

import vlc

def get_audio_duration(filepath):
    
    
    instance = vlc.Instance()
    
    media = instance.media_new(filepath)
    
    player = instance.media_player_new()
    player.set_media(media)
    
    media.parse_with_options(1,0)
    
    while True:
        if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
            break
        
    #player.play()
        
    return(media.get_duration())

print(get_audio_duration('input/mp3/start.wav'))