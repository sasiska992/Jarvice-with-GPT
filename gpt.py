import asyncio
import time

from g4f.client import Client
import pynput
from pynput.keyboard import Controller, Key, HotKey


async def create_gpt_promt(promt: str) -> str:
    client = Client()
    promt += (
        ". Сделай это так, будто это написан код. То есть пришли текст без ``` и свои комментарии оберни в комментарии python. "
        "Не пиши вспомогательный текст. Просто выполни запрос"
        "Мне нужно будет записать твой текст в файл. Вместо отступов в начале строк пиши перенос каретки. "
        "НЕ ПИШИ ЛИШНИЕ КОММЕНТАРИИ. "
        "Приведи пример использования через # Пример использования:")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": promt}],
    )
    return response.choices[0].message.content


def go_to_start():
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.press(Key.esc)
    keyboard.press("0")
    keyboard.press("i")


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
            go_to_start()
            keyboard.press("#")
        else:
            time.sleep(0.5)
            keyboard.press(value[index])
    keyboard.press(Key.ctrl)
    keyboard.press(Key.alt)
    keyboard.press('l')

    # Отпускаем L, затем Alt и Ctrl
    keyboard.release('l')
    keyboard.release(Key.alt)
    keyboard.release(Key.ctrl)


def write_something_test(value: str):
    keyboard = Controller()
    # value = value.replace("    ", "")
    # value = value.replace("\t", "")
    # example_of_use = value.index("# Пример использования:")
    value = value.split("\n")
    for index in range(len(value)):
        # elif value[index] == "\t":
        #     keyboard.press(Key.tab)
        keyboard.type(value[index])
        go_to_start()
        time.sleep(0.1)

    time.sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press(Key.alt)
    keyboard.press('l')

    # Отпускаем L, затем Alt и Ctrl
    keyboard.release('l')
    keyboard.release(Key.alt)
    keyboard.release(Key.ctrl)


if __name__ == "__main__":
    time.sleep(2)
    # go_to_start()
    result = asyncio.get_event_loop().run_until_complete(create_gpt_promt(
        "напиши quick sort на python"))
    print(result)
    write_something(result)
