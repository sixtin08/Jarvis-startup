import tkinter as tk
import pygame
import time
import sys
import os

# ---------------- RESOURCE PATH FIX (IMPORTANT) ----------------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # when running as EXE
    except Exception:
        base_path = os.path.abspath("")  # when running normally

    return os.path.join(base_path, relative_path)


# ---------------- AUDIO + UI ----------------
def play_audio_and_close():
    pygame.mixer.init()

    audio_file = resource_path("jarvis.mp3")
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # wait until audio finishes
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    root.destroy()


# ---------------- UI SETUP ----------------
root = tk.Tk()
root.title("JARVIS")

root.configure(bg="black")
root.overrideredirect(True)

width = 500
height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

root.geometry(f"{width}x{height}+{x}+{y}")

label = tk.Label(
    root,
    text="JARVIS SYSTEM ONLINE\nSTUDY MODE ON",
    fg="cyan",
    bg="black",
    font=("Consolas", 14),
    justify="center"
)
label.pack(expand=True)


# ---------------- START AUDIO ----------------
root.after(100, play_audio_and_close)

root.mainloop()