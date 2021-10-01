import socket
import vgamepad as vg
from _thread import *
import sys

server = "192.168.0.103"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen()
print("Waiting for a connection, Server started")


try:
    gamepad = vg.VX360Gamepad()
    from keys_xbox import keys_dict, keys_joystick, keys_triggers, reset_buttons, press_buttons
except:
    try:
        gamepad = vg.VDS4Gamepad()
        from keys_ps import keys_dict, keys_joystick, keys_triggers, reset_buttons, press_buttons
    except:
        sys.exit()


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    while True:
        data = conn.recv(256)
        reply = data.decode("utf-8")
        if not data:
            print("Disconnected")
            break

        else:

            reset_buttons(gamepad)
            received = reply.split(":")[0]
            print("Received ", received)
            all_keys = received.split(',')
            press_buttons(gamepad, all_keys)
            gamepad.update()


accept_addr = "192.168.0.103"

if __name__ == "__main__":
    while True:
        conn, addr = s.accept()
        print("Connected to ", addr)
        start_new_thread(threaded_client, (conn,))
