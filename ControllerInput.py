from inputs import get_gamepad
import KeyboardShortcuts as KS

def Run():
    JL = JR = TL = TR = PB = False
    next = prev = pause = False
    
    while True:
        events = get_gamepad()
        for event in events:
            if event.code == 'BTN_TL':
                if TL:
                    TL = False
                    prev = False
                else:
                    TL = True

            if event.code == 'BTN_TR':
                if TR:
                    TR = False
                    next = False
                else:
                    TR = True

            if event.code == 'BTN_THUMBL':
                if JL:
                    JL = False
                else:
                    JL = True

            if event.code == 'BTN_THUMBR':
                if JR:
                    JR = False
                else:
                    JR = True

            if event.code == 'BTN_SELECT':
                if PB:
                    PB = False
                    pause = False
                else:
                    PB = True

        if TL and TR:
            if PB and not pause:
                KS.PauseSong()
                pause = True

        if JL and JR:
            if TR and not next:
                KS.NextSong()
                next = True
            if TL and not prev:
                KS.PrevSong()
                prev = True