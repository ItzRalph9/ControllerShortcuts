import tkinter
import sys
from random import randrange

# Local programs
import UIElements as UIE
import ControllerThread as CT

# Constants
BG_COLOR = '#272e36'
TXT_COLOR = '#eeeeee'

# create a GUI window
root = tkinter.Tk()
root.title("Controller Shortcuts")

list = [True,False,True,3,1]
print(all(list))

def SetRandomColor():
    color = f'#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256))
    root.configure(background=color) 

button = tkinter.Button(root, text="Set background color", command = SetRandomColor)
button.place(relx=0.5, rely=0.87, anchor='center')

x = 760 # x offset to set window in center
y = 340 # y offset to set window in center
root.geometry(f'{400}x{200}+{x}+{y}')
root.resizable(False, False)
root.configure(background=BG_COLOR) 

photo = tkinter.PhotoImage(file = "controller.png")
root.iconphoto(False, photo)

UIE.ConstructUIElements(root, BG_COLOR, TXT_COLOR)
CT.createThread()

def onClose():
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", onClose)

root.mainloop()