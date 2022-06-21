from pynput.mouse import Listener

click_counter = 0

def on_click(x, y, button, pressed):
    if pressed:
        global click_counter
        click_counter += 1
        print("Mouse clicked")
        print(click_counter)

with Listener(on_click=on_click) as listener:
    listener.join()