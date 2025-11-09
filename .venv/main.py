import speech_recognition as sr
import json
import os
import subprocess
import random
from playsound import playsound
import time  # для паузы между итерациями

# === Функция воспроизведения готового mp3 ===
def say(key):
    """
    key — ключ команды, например 'open_music' или 'not_understood'.
    Выбирает случайный mp3 для этой команды и воспроизводит.
    """
    folder = "audio"
    files = [f for f in os.listdir(folder) if f.startswith(key)]
    if not files:
        print(f"[!] Нет аудио для {key}")
        return
    file = os.path.join(folder, random.choice(files))
    playsound(file)

# === из JSON читаю файлики ===
with open("commands.json", encoding="utf-8") as f:
    commands = json.load(f)["команды"]

# === Тут действия делаются ===
def execute_action(action):
    if action == "open_music":
        music_path = r"C:\Users\GvinBlade\Music"
        os.startfile(music_path)
        say("open_music")  # ключ mp3

    elif action == "open_android_studio":
        studio_path = r"D:\AndStud\bin\studio64.exe"
        if os.path.exists(studio_path):
            subprocess.Popen(studio_path)
            say("open_android_studio")
        else:
            say("not_found")

    elif action == "restart_pc":
        say("restart_pc")
        subprocess.run(["shutdown", "/r", "/t", "5"])

    elif action == "shutdown_pc":
        say("shutdown_pc")
        subprocess.run(["shutdown", "/s", "/t", "5"])

    else:
        say("unknown_command")

# === что я говорю ===
def process_command(user_text):
    for cmd in commands:
        for phrase in cmd["фразы"]:
            if phrase.lower() in user_text.lower():
                execute_action(cmd["действие"])
                return True
    say("unknown_command")
    return False

# === Вечный цикл ===
r = sr.Recognizer()

try:
    while True:
        with sr.Microphone() as source:
            print("Настройка уровня шума...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Слушаю команду...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        try:
            text = r.recognize_google(audio, language="ru-RU")
            print("Распознано:", text)
            process_command(text)
        except sr.UnknownValueError:
            say("unknown_command")
        except sr.RequestError as e:
            say("service_error")

        time.sleep(0.5)  # небольшая пауза между итерациями

except KeyboardInterrupt:
    print("Выход из программы по Ctrl+C")
