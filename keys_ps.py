import vgamepad as vg

bt = vg.DS4_BUTTONS
special_bt = vg.DS4_SPECIAL_BUTTONS
keys_dict = {'Key.esc': bt.DS4_BUTTON_SHARE,  # Join game
             'Key.up': bt.DS4_BUTTON_TRIANGLE,  # Shoot up
             'Key.down': bt.DS4_BUTTON_CROSS,  # Shoot down
             'Key.left': bt.DS4_BUTTON_SQUARE,  # Shoot left
             'Key.right': bt.DS4_BUTTON_CIRCLE,  # Shoot right
             "'q'": bt.DS4_BUTTON_SHOULDER_RIGHT,  # Drop item
             "'e'": bt.DS4_BUTTON_SHOULDER_LEFT,  # Use item
             'Key.ctrl_l': bt.DS4_BUTTON_TRIGGER_RIGHT,  # Drop item
             'Key.space': bt.DS4_BUTTON_TRIGGER_LEFT,  # Use item
             }

keys_joystick = {"'w'": (1, 120),  # Move up
                 "'a'": (0, -120),  # Move left
                 "'s'": (1, -120),  # Move down
                 "'d'": (0, 120),  # Move right
                 }
keys_special = {
    'Key.tab': special_bt.DS4_SPECIAL_BUTTON_TOUCHPAD
}

keys_triggers = (
    "'q'",  # Drop item
    "'e'"  # Use item
)


def press_buttons(gamepad, all_keys):
    x_y = [128, 128]
    for key in keys_joystick:
        if key in all_keys:
            value = keys_joystick[key]
            x_y[value[0]] += value[1]

    gamepad.left_joystick(*x_y)
    for k in all_keys:
        if k in keys_dict:
            gamepad.press_button(keys_dict[k])


def reset_buttons(gamepad):
    for keys in keys_dict.values():
        gamepad.release_button(keys)
    gamepad.left_trigger(0)
    gamepad.right_trigger(0)
