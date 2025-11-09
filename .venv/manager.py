import json
import os
import pyttsx3
import subprocess

tts = pyttsx3.init()
tts.setProperty('volume', 1.0)
tts.setProperty('rate', 160)

def say(text):
    print("Джарвис говорит:", text)
    tts.say(text)
    tts.runAndWait()

with open ("config.json", encoding="utf-8") as f:
    commands = json.load(f)["команды"]

def execute_action(action):
    """Действия по ключу. Если сказать 'включи музыку' - сработает action_music"""

    if action == "open_music":
        music_path = r"C:\Users\GvinBlade\Music"
        os.startfile(music_path)
        say("Включаю, сэр")
    elif action == "open_android_studio":
        android_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Android Studio"
        subprocess.Popen(android_path)
        say("Пожуйте говна, Сэр")
    elif action == "restart_pc":
        say("Сейчас вернусь, кожаный!")
        subprocess.run("shutdown /r /t 5", shell = True)
    elif action == "shutdown_pc":
        say("Не убивай, кожаный!")
        subprocess.run("shutdown /t 5", shell=True)
    else:
        say("Не знаю такой команды, Сэр")
def process_command(user_text):
    """"Поиск Команды в JSON"""
    for cmd in commands:
        for phrase in cmd["фразы"]:
            if phrase.lower() in user_text.lower():
                execute_action(cmd["действие"])
                return True
    say("Команда не распознана, Сэр")
    return False