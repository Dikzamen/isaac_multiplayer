import socket
import time
from _thread import start_new_thread
from pynput import keyboard

isaac_keys = ['Key.esc', "'w'", "'a'", "'s'", "'d'", 'Key.up', 'Key.down',
              'Key.left', 'Key.right', 'Key.ctrl_l', "'e'", 'Key.space', "'q'", 'Key.tab']


def on_press(key):
    global pressed_buttons
    print(str(key))
    if not ((str(key)) in isaac_keys):
        return
    if str(key) not in pressed_buttons:
        pressed_buttons.append(str(key))


def on_release(key):
    global pressed_buttons
    if str(key) in pressed_buttons:
        pressed_buttons.remove(str(key))
    pass


def connect(client, addr):
    client.connect(addr)
    print("Network recieved ", client.recv(512).decode())
    counter = 0
    last_msg = []
    while True:
        time.sleep(.02)
        global pressed_buttons
        counter += 1
        if pressed_buttons != last_msg:
            my_str = ','.join(pressed_buttons)
            print("Sending  ", my_str)
            client.send(str.encode(f"{my_str}:"))


def pressing_func(_):
    global pressed_buttons
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()


pressed_buttons = []
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "192.168.0.103"
port = 5555
addr = (server, port)
i = 1
start_new_thread(pressing_func, (i,))
connect(client, addr)
