import os
import asyncio
import json
import edge_tts

# Папка для mp3
folder = "audio"
os.makedirs(folder, exist_ok=True)

# Голос
voice = "ru-RU-SvetlanaNeural"

# Загружаем фразыыыыы
with open("phrases.json", encoding="utf-8") as f:
    phrases = json.load(f)

async def generate_mp3(text, filename):
    communicate = edge_tts.Communicate(text, voice=voice)
    await communicate.save(filename)

async def main():
    for key, variants in phrases.items():
        for i, text in enumerate(variants, start=1):
            filename = os.path.join(folder, f"{key}_{i}.mp3")
            print(f"Генерируем: {filename}")
            await generate_mp3(text, filename)

asyncio.run(main())
print("Генерация mp3 завершена!")
