from pynput import mouse
import time
import turtle


def on_move(x, y):
    print("Pointer moved to {0}".format(x, y))
    time.sleep(0.5)


def on_click(x, y, button, pressed):
    print("{0} at {1}".format(
        "Pressed" if pressed else "Released", (x, y)))
    time.sleep(0.5)


def on_scroll(x, y, dx, dy):
    print("Scrolled {0}".format(x, y))
    time.sleep(0.5)


with Listener(
    on_move=on_move,
    on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
    time.sleep(0.5)


