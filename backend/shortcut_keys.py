from pynput.keyboard import Key, Controller

keyboard = Controller()
def play_pause():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    return "play/pause (SPACE)"
def fullscreen():
    keyboard.press("f")
    keyboard.release("f")
    return "fullscreen (f)"
def mute():
    keyboard.press("m")
    keyboard.release("m")
    return "mute (m)"
def next_video():
    keyboard.press(Key.shift)
    keyboard.press("n")
    keyboard.release("n")
    keyboard.release(Key.shift)
    return "next video (SHIFT + n)"
def skip_10percent():
    keyboard.press("1")
    keyboard.release("1")
    return "skip 10% (1)"
    
def run_shortcut(count):
    # Depending on detected # of raised fingers... 
    shortcuts = {
        1: play_pause,
        2: fullscreen,
        3: mute,
        4: next_video,
        5: skip_10percent
    }
    if count in shortcuts:
        return shortcuts[count]()
    return None
