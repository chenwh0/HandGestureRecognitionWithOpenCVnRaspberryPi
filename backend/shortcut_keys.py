from ShortcutKeys import *

def run_shortcut(count):
    # Depending on detected # of raised fingers... 
    shortcuts = {
        1: jump_10percent,
        2: fullscreen,
        3: mute,
        4: next_video,
        5: play_pause
    }
    if count in actions:
        actions[count]()
