#https://www.pythontutorial.net/tkinter/tkinter-hello-world/

import tkinter as tk
from tkinter import ttk
import time

# Instance of the tk.Tk class that creates the window:
root = tk.Tk()
# change title of the window
root.title('Demo')

# change icon showing at the top (.ico file must be used)
root.wm_iconbitmap('barcelona.ico')

# reads the current title of the window
title = root.title()
print(title)

# read screen size


# choose size in pixels of the window
window_width = 800
window_height = 800

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

'''
size of the window (widthxheight±x±y)
width is the width in pixels, height the height in pixels,
x is pixels distance from the windows to the screen edge
if x positive: between left edge of window and screen
if x negative: between right edge of window and screen
y, the same but for vertical. if y positive, distance in top, if negative in bottom
'''
# we are going to horizontally center the window in the screen and put it in the top
center_x = int(screen_width/2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+0')

# we can say if the windows can be resized in any of both directions
# in this case, only vertically will be possible
root.resizable(False, True)

# a maximum and minimum size of the screen can be defined when resizing the windows
min_height = 200
min_width = 200
max_height = 1000
max_width = 1000
root.minsize(min_height, min_width)
root.maxsize(max_height, max_width)

# it can be specified the transparency of the window from 0.0 to 1.0
root.attributes('-alpha',1.0)

# to specifiy that the window is always opened at the front of other programs
# even if be ty to put some above, put -topmost to 1
root.attributes('-topmost', 0)

# to put a window up or down the stack of programs opened, use lift and lower
# in this case, it is put down of all but at the same time put at front again
root.lower()
root.lift()




# displays a label for the window
label = ttk.Label(root)
label['text'] = 'Hola tio'
label.pack()

#other way -->
#    label = ttk.Label(root)
#    label.config(text='Hi, there')
#    label.pack()


# it can be asociated an action when an event occurs to a widget
# not all widgets, only button and few others
# only mouse and backspace jey affect it, not the return key

# a fucntion is defined to call when the event happens
def button_clicked():
    print('Has pulsado el botón')

# the function can now be associated to a widget, a new created button
button = ttk.Button(root, text='Click Me', command=button_clicked).pack()

# now, a function that accepts arguments
def show_color(color):
    print(color)

# and the function is assigned to two buttons, which use the same function
# but with different argument
button_blue = ttk.Button(
    root,
    text='Blue',
    command = lambda: show_color('Blue')).pack()

button_red = ttk.Button(
    root,
    text='Red',
    command = lambda: show_color('Red')).pack()


# another way to bind an action to a en event is using bind, which offers more options
# a new function will be used for the new button.
# for this functions, it must be put an argument event if not used
def say_hi(sd):
    print('Hiiiiii')

button_green = ttk.Button(
    root,
    text='Green')

# now, when the return key is pressed, the show_color function is executed
# The first argument defines which is the action on the button to consider
# the structure is <modifier-type-detail>
# examples in https://www.pythontutorial.net/tkinter/tkinter-event-binding/

button_green.bind('<Return>', say_hi)

# it can be add more action to the same event with the parameter add equal to +
# we will create a new function to execute at the sime time
def say_bye(event):
    print('Byeee')

button_green.bind('<Return>', say_bye, add='+')

# once defined the button, add it to the window
button_green.focus()
button_green.pack(expand=True)


# it is posible to assign buttons to the window aswell (the top one if several)
# new function used for it
def quepasa(event):
    print('QUE PASAA')

root.bind('<Return>', quepasa)


# it can also be binded an event to all the instances of the same class
root.bind_class('Entry', '<Control-V>', button_clicked)


# it can also be unbinded an event
# segun se configura antes, al usar la tecla return sobre el boton verde
# se activarian dos funciones, pero ya no ocurre con el unbind
button_green.unbind('<Return>')


# a label can be customized with options
label_color = ttk.Label(
            root, 
            text='Otro boton',
            font=("Helvetica", 18))

# ipadx and ipady can be used to move the label
label_color.pack(ipadx=50, ipady=50)

# un label tambien puede poner una imagen
# para poner texto e imagen junto, usar compound que define
# donde va la imagen respecto el texto (top, borttom, left, right)
photo = tk.PhotoImage(file='barcelona.png')
label_imagen = ttk.Label(
            root, 
            text='FC Barcelona',
            image=photo,
            padding=50,
            compound='top').pack()







# function to avoid the window to be blurry
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    # call method to keep windows open
    root.mainloop()
