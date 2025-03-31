import os
import pygame
from pynput import keyboard

pygame.mixer.init()

tracks = [
    "/Users/azamat/Documents/GitHub/PP2/LAB/lab7/Wu-Kang.mp3",
    "/Users/azamat/Documents/GitHub/PP2/LAB/lab7/Qyz Bozbala.mp3",
    "/Users/azamat/Documents/GitHub/PP2/LAB/lab7/Die With A Smile.mp3"
]
current_track_index = 0

def play_track():
    pygame.mixer.music.load(tracks[current_track_index])
    pygame.mixer.music.play()

def stop_track():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(tracks)
    play_track()

def prev_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(tracks)
    play_track()

def exit_program():
    pygame.mixer.quit()
    os._exit(0)

def on_press(key):
    try:
        if key == keyboard.Key.space:
            play_track()
        elif hasattr(key, 'char') and key.char == "s":
            stop_track()
        elif hasattr(key, 'char') and key.char == "n":
            next_track()
        elif hasattr(key, 'char') and key.char == "p":
            prev_track()
        elif hasattr(key, 'char') and key.char == "q":
            exit_program()
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

listener.join()