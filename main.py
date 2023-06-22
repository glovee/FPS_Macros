from pynput import mouse, keyboard
import pyautogui as pag
import time



start = 1
close = 0
end_main = 1



def weapon_ready():
    global start
    if start == 1:
        pag.move(2, 7, 0.09)
        start += 1
    elif start == 2:
        pag.move(-5, 7, 0.09)
        start += 1
    elif start == 3:
        pag.move(2, 3, 0.09)
        start += 1
    elif start == 4:
        pag.move(2, 7, 0.09)
        start += 1
    elif start == 5:
        pag.move(-5, 7, 0.09)
        start = 1

def on_press(key):
    time.sleep(0.001)
    if key == keyboard.Key.end:
        global end_main
        end_main = 0


def on_click(x, y, button, pressed):
    time.sleep(0.001)
    global close
    if pressed:
        if button == mouse.Button.left:
            close = 1
    else:
        if button == mouse.Button.left:
            close = 0

klistener = keyboard.Listener(
    on_press=on_press)
klistener.start()

listener = mouse.Listener(
    on_click=on_click)
listener.start()


while end_main:
    time.sleep(0.001)
    if close:
        weapon_ready()