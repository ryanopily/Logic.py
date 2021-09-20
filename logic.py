import keyboard

wording = ""
hook = 0

code_lookup = {
    # Logic
    "forall": "∀",
    "exists": "∃",
    "implies": "→",
    "iff" : "↔",
    "not" : "¬",
    "and" : "∧",
    "or"  : "∨",
    "xor" : "⊕",
    "top" : "⊤",
    "bottom" : "⊥",
    "def": "≡",
    "proves": "⊢",
    "models": "⊨",

    # Set theory
    "int": "⋂",
    "union": "⋃",
    "subset": "⊆",
    "psubset": "⊂",
    "nsubset": "⊄",
    "superset": "⊇",
    "psuperset": "⊃",
    "nsuperset": "⊅",
    "elem": "∈",
    "nelem": "∉",
    "prod": "×",
    "empty": "Ø"
}

def onPress(keyboard_event):
    global wording

    # When enter is pressed, type out lookup key value.
    if keyboard_event.scan_code == 28:
        if wording in code_lookup:
            keyboard.write(code_lookup[wording])
        wording = ""
        stop()
        
    # Add key typed to lookup key
    else: wording += keyboard_event.name

# Start recording keyboard input
def start():
    global onPress, hook
    hook = keyboard.on_press(onPress, suppress=True)

# Stop recording keyboard input
def stop():
    global onPress, hook
    keyboard.unhook(hook)

# Press Ctrl + L to lookup logic/set theory symbol
keyboard.add_hotkey("ctrl+l", start)
