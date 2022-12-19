from evdev import InputDevice, categorize, ecodes

ABShutter3 = InputDevice('/dev/input/event5')

EV_VAL_PRESSED = 1
EV_VAL_RELEASED = 0
BTN_SHUTTER = 115

print(ABShutter3)

for event in ABShutter3.read_loop():
    if event.type == ecodes.EV_KEY:
        print(event)
        print(categorize(event))