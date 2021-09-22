# -*- coding: utf-8 -*-



import time
import vlc


cool_duration = 20
work_duration = 40
global_duration = 60 * 60


# %%

def get_audio_duration(filepath):
    
    
    instance = vlc.Instance()
    
    media = instance.media_new(filepath)
    
    player = instance.media_player_new()
    player.set_media(media)
    
    media.parse_with_options(1,0)
    
    while True:
        if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
            break
        
    return(player, media.get_duration()/1000)


# %% Main


loop_time = time.time()
global_time = time.time()

stop = False
phase = 'cooldown'
audio_play = False
last_int = 0

start_player, start_audio_duration = get_audio_duration('input/mp3/start.wav')
stop_player, stop_audio_duration = get_audio_duration('input/mp3/stop.flac')


cool_audio_duration = cool_duration - start_audio_duration
work_audio_duration = work_duration - stop_audio_duration

while stop == False:
    
    cur_time = time.time()
    
    if phase == 'cooldown':
        
        # print countdown time
        new_int = int(cur_time - loop_time)
        if new_int != last_int:
            last_int = new_int
            print(int(cool_duration) - new_int)
    
        # play start audio
        if cur_time - loop_time > cool_audio_duration and audio_play == False:
            start_player.play()
            audio_play = True
            
        elif cur_time - loop_time > cool_duration:
            start_player, start_audio_duration = get_audio_duration('input/mp3/start.wav')
            audio_play = False
            phase = 'workout'
            loop_time = time.time()
            print('workout started')
            
    elif phase == 'workout':
        
        # print countdown time
        new_int = int(cur_time - loop_time)
        if new_int != last_int:
            last_int = new_int
            print(int(work_duration) - new_int)
        
        # play stop audio
        if cur_time - loop_time > work_audio_duration and audio_play == False:
            stop_player.play()
            audio_play = True
            
        elif cur_time - loop_time > work_duration:
            stop_player, stop_audio_duration = get_audio_duration('input/mp3/stop.flac')
            audio_play = False
            phase = 'cooldown'
            loop_time = time.time()
            print('Cooldown Started')
            
    # Ending Condition
    if cur_time - global_time > global_duration:
        stop = True
            
            




















