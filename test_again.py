import pyautogui
import time
import mouse
import keyboard

# Флаг для остановки движения мыши
stop_mouse = False

# Функция-обработчик события нажатия кнопки мыши
def event_listener(event):
    global stop_mouse  # Используем глобальный флаг
    if isinstance(event, mouse.ButtonEvent):
        if event.event_type == 'down' and event.button == 'left':  # Исправляем названия атрибутов
            while not stop_mouse:  # Изменяем условие выхода из цикла
                pyautogui.move(1, 7)
                if isinstance(event, mouse.ButtonEvent):
                    if event.event_type == 'up' and event.button == 'left':  # Исправляем названия атрибутов
                        break

# Регистрируем функцию-обработчик для событий мыши
mouse.hook(event_listener)

# Регистрируем функцию-обработчик для событий клавиатуры
keyboard.hook(event_listener)

# Функция для установки флага stop_mouse
def stop_mouse_func():
    global stop_mouse
    stop_mouse = True

keyboard.wait()  # Удаляем аргумент "ESC" в функции keyboard.wait()
