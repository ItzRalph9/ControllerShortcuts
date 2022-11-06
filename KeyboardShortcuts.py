from pyautogui import hotkey

def PauseSong():
    hotkey('ctrl', 'alt', 'space')

def NextSong():
    hotkey('ctrl', 'alt', 'right')

def PrevSong():
    hotkey('ctrl', 'alt', 'left')