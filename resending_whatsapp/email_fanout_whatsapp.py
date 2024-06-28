import os
import webbrowser
from urllib.parse import quote
import pyautogui
import asyncio
import time
import psutil

# Проверяем, что файл phones.txt существует
if not os.path.isfile("phones.txt"):
    print("Файл phones.txt не найден.")
    exit()

with open("phones.txt", "r") as phones_file:
    phones_and_names_list = phones_file.readlines()

screen_width, screen_height = pyautogui.size()


async def close_firefox():
    """
    Asynchronously closes all running Firefox processes to avoid a mess.
    This function iterates over all running processes and checks if the process name is 'firefox'. If a Firefox process is found, it attempts to kill the process. Any exceptions raised during the process of killing the process are caught and ignored.
    This function does not return any value.
    """
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'firefox':
            try:
                proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass


async def send_message(phone, name):
    try:
        message = f"Здравствуйте {name}! У нас началась распродажа! Скидки до -30%!"
        encoded_message = quote(message)

        # Закрываем Firefox перед открытием новой вкладки
        await close_firefox()

        # Открываем WhatsApp Web и ждем, пока страница загрузится
        webbrowser.open(

            f"https://web.whatsapp.com/send?phone={phone}&text={encoded_message}"
        )
        await asyncio.sleep(8)

        # Отправляем сообщение
        pyautogui.click(screen_width / 2, screen_height / 2)
        pyautogui.press("enter")
        await asyncio.sleep(3)

        # Закрываем вкладку
        pyautogui.hotkey("command", "w")
    except Exception as e:
        print(f"Ошибка при отправке сообщения для номера {phone}: {e}")


async def main():
    for row in phones_and_names_list:
        row_list = row.split(",")
        phone = row_list[0].strip()
        name = row_list[1].strip()
        await send_message(phone, name)

    # Информируем, что все сообщения отправлены
    print("Все сообщения отправлены.")

if __name__ == "__main__":
    asyncio.run(main())
