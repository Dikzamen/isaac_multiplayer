import vgamepad as vg
bt = vg.XUSB_BUTTON

keys_dict = {'Key.esc': bt.XUSB_GAMEPAD_START,                  # Join game
             'Key.up': bt.XUSB_GAMEPAD_Y,                       # Shoot up
             'Key.down': bt.XUSB_GAMEPAD_A,                     # Shoot down
             'Key.left': bt.XUSB_GAMEPAD_X,                     # Shoot left
             'Key.right': bt.XUSB_GAMEPAD_B,                    # Shoot right
             "'e'": bt.XUSB_GAMEPAD_LEFT_SHOULDER,              # Use bomb
             "'q'": bt.XUSB_GAMEPAD_RIGHT_SHOULDER,             # Use pill/card
             'Key.tab': bt.XUSB_GAMEPAD_BACK                    # Open map
             }

keys_joystick = {"'w'": (1, 32000),                             # Move up
                 "'a'": (0, -32000),                            # Move left
                 "'s'": (1, -32000),                            # Move down
                 "'d'": (0, 32000),                             # Move right
                 }

keys_triggers = {'Key.ctrl_l': bt.XUSB_GAMEPAD_RIGHT_THUMB,     # Drop item
                 'Key.space': bt.XUSB_GAMEPAD_LEFT_THUMB,       # Use item
                 }


def press_buttons(gamepad, all_keys):
    x_y = [0, 0]
    for key in keys_joystick:
        if key in all_keys:
            value = keys_joystick[key]
            x_y[value[0]] += value[1]

    for key in keys_triggers:
        if key == "Key.ctrl_l" and key in all_keys:
            gamepad.left_trigger(255)
        if key == "Key.space" and key in all_keys:
            gamepad.right_trigger(255)

    gamepad.left_joystick(*x_y)
    for k in all_keys:
        if k in keys_dict:
            gamepad.press_button(keys_dict[k])


def reset_buttons(gamepad):
    for keys in keys_dict.values():
        gamepad.release_button(keys)
    gamepad.left_trigger(0)
    gamepad.right_trigger(0)
