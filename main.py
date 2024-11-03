import asyncio
import time
from turtle import Screen

import requests
import speech_recognition
from pydub import AudioSegment
from pydub.playback import play
import os
from pynput.keyboard import Key, Controller
from pathlib import Path

from draw import draw_sierpinski
from gpt import create_gpt_promt, write_something_to_file


def download_random_cat_image():
    # URL для получения случайного изображения котика
    url = "https://api.thecatapi.com/v1/images/search"

    # Запрос к API
    response = requests.get(url)

    if response.status_code == 200:
        # Получаем URL изображения из ответа
        cat_image_url = response.json()[0]['url']

        # Скачиваем изображение
        image_response = requests.get(cat_image_url)

        if image_response.status_code == 200:
            # Сохраняем изображение
            with open("random_cat.jpg", "wb") as file:
                file.write(image_response.content)
            print("Случайное изображение котика скачано и сохранено как random_cat.jpg")
        else:
            print("Не удалось скачать изображение котика.")
    else:
        print("Не удалось получить URL изображения котика.")


def write_something(value: str):
    keyboard = Controller()
    value = value.replace("    ", "")
    value = value.replace("\t", "")
    example_of_use = value.index("# Пример использования:")
    for index in range(len(value)):
        if value[index] == "\n":
            keyboard.press(Key.enter)
            time.sleep(0.1)
            index += 1
        elif value[index] == "\t":
            keyboard.press(Key.tab)
        elif index == example_of_use:
            keyboard.press(Key.esc)
            keyboard.press("0")
            keyboard.press("i")
            keyboard.press("#")
        else:
            time.sleep(0.01)
            keyboard.press(value[index])
    time.sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press(Key.alt)
    keyboard.press('l')

    # Отпускаем L, затем Alt и Ctrl
    keyboard.release('l')
    keyboard.release(Key.alt)
    keyboard.release(Key.ctrl)


def run_draw_sierpinski():
    draw_sierpinski()  # Запускаем функцию рисования


# Вызов функции
sr = speech_recognition.Recognizer()
# sr.pause_threshold = 0.5

sounds = {
    "джарвис": "sounds\Доброе утро.wav",
    "привет": "sounds\Доброе утро.wav",
    "я гей": "sounds\Судя по всему, использование костюма железного человека усугубляет ваше состояние.wav",
    "где я": "sounds\Район Нью-Йорка, Манхэттэн и окрестности.wav",
    "экстренная перезагрузка": "sounds",
}
with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic)
    # audio = AudioSegment.from_wav("sounds\Джарвис - приветствие.wav")
    # play(audio)
    while True:
        print("Началась проверка...")
        audio = sr.listen(source=mic)
        print("Делается запрос")
        try:
            query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
            if query == "джарвис" or query == "привет":
                audio = AudioSegment.from_wav("sounds\Доброе утро.wav")
            elif query == "где я":
                audio = AudioSegment.from_wav("sounds\Район Нью-Йорка, Манхэттэн и окрестности.wav")
            elif query == "экстренная перезагрузка":
                audio = AudioSegment.from_wav("sounds\Начинаю диагностику системы.wav")
                play(audio)
                audio = AudioSegment.from_wav("sounds\windows-xp-shutdown.wav")
                play(audio)
                audio = AudioSegment.from_wav("sounds\Запрос выполнен сэр.wav")
            elif query == "молодец":
                audio = AudioSegment.from_wav("sounds\Всегда к вашим услугам сэр.wav")
            elif query == "покажи котика":
                path = Path.cwd()
                download_random_cat_image()
                os.startfile(str(path) + r'\random_cat.jpg')
                audio = AudioSegment.from_wav("sounds\Запрос выполнен сэр.wav")
            elif query == "напиши":
                result = asyncio.get_event_loop().run_until_complete(create_gpt_promt(
                    "напиши какой-то сложный алгоритм на python. Не пиши установочные библиотеки"))
                print(result)
                write_something_to_file(result)
            elif query == "нарисуй":
                print("Запустите файл draw.py")
                audio = AudioSegment.from_wav("sounds\Запрос выполнен сэр.wav")
            else:
                audio = AudioSegment.from_wav("sounds\Чего вы пытаетесь добиться сэр.wav")
            play(audio)
        except Exception as e:
            print("Не удалось распознать звук")
