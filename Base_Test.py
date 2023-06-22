import keyboard
import mouse
import time
 
 
def event_listener(event):
    if isinstance(event, mouse.MoveEvent):
        print(event)
    elif isinstance(event, mouse.ButtonEvent):
        print(event)
    elif isinstance(event, keyboard.KeyboardEvent):
        print(event)
        
 
 
mouse.hook(event_listener)
keyboard.hook(event_listener)
 
keyboard.wait("ESC")