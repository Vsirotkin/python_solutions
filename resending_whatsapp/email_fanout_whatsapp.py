# import os
# import webbrowser
# from urllib.parse import quote
# import pyautogui
# import asyncio
# import time
# import psutil

# # Проверяем, что файл phones.txt существует
# if not os.path.isfile("phones.txt"):
#     print("Файл phones.txt не найден.")
#     exit()

# with open("phones.txt", "r") as phones_file:
#     phones_and_names_list = phones_file.readlines()

# screen_width, screen_height = pyautogui.size()


# async def close_firefox():
#     """
#     Asynchronously closes all running Firefox processes to avoid a mess.
#     This function iterates over all running processes and checks if the process name is 'firefox'. If a Firefox process is found, it attempts to kill the process. Any exceptions raised during the process of killing the process are caught and ignored.
#     This function does not return any value.
#     """
#     for proc in psutil.process_iter(['pid', 'name']):
#         if proc.info['name'] == 'firefox':
#             try:
#                 proc.kill()
#             except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#                 pass


# async def send_message(phone, name):
#     try:
#         message = f"Здравствуйте {name}! У нас началась распродажа! Скидки до -30%!"
#         encoded_message = quote(message)

#         # Закрываем Firefox перед открытием новой вкладки
#         await close_firefox()

#         # Открываем WhatsApp Web и ждем, пока страница загрузится
#         webbrowser.open(

#             f"https://web.whatsapp.com/send?phone={phone}&text={encoded_message}"
#         )
#         await asyncio.sleep(8)

#         # Отправляем сообщение
#         pyautogui.click(screen_width / 2, screen_height / 2)
#         pyautogui.press("enter")
#         await asyncio.sleep(3)

#         # Закрываем вкладку
#         pyautogui.hotkey("command", "w")
#     except Exception as e:
#         print(f"Ошибка при отправке сообщения для номера {phone}: {e}")


# async def main():
#     for row in phones_and_names_list:
#         row_list = row.split(",")
#         phone = row_list[0].strip()
#         name = row_list[1].strip()
#         await send_message(phone, name)

#     # Информируем, что все сообщения отправлены
#     print("Все сообщения отправлены.")

# if __name__ == "__main__":
#     asyncio.run(main())


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from urllib.parse import quote
import time
import asyncio

# Check if the phones.txt file exists
phones_file_path = Path("phones.txt")
if not phones_file_path.is_file():
    print("Файл phones.txt не найден.")
    exit()

with open(phones_file_path, "r") as phones_file:
    phones_and_names_list = phones_file.readlines()


async def send_message(driver, phone, name):
    try:
        message = f"Здравствуйте {name}! У нас началась распродажа! Скидки до -30%!"
        encoded_message = quote(message)
        url = f"https://web.whatsapp.com/send?phone={phone}&text={encoded_message}"

        # Open WhatsApp Web and wait for the page to load
        driver.get(url)
        await asyncio.sleep(
            30
        )  # Add a delay of 30 seconds to allow the page to fully load

        # Wait for the input box to be available
        input_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    '.selectable-text.copyable-text[data-lexical-text="true"]',
                )
            )
        )

        # Find and click the send button based on the title attribute
        for _ in range(3):
            try:
                send_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (
                            By.CSS_SELECTOR,
                            'button[aria-label="Отправить"], button[aria-label="Send"]',
                        )
                    )
                )
                ActionChains(driver).move_to_element(send_button).click().perform()
                break
            except Exception as e:
                print(f"Retry attempt {_ + 1}: {e}")
                await asyncio.sleep(1)

        await asyncio.sleep(5)

    except Exception as e:
        print(f"Ошибка при отправке сообщения для номера {phone}: {e}")


async def main():
    firefox_options = Options()
    firefox_options.add_argument("--start-minimized")
    service = Service("/usr/bin/geckodriver")
    driver = webdriver.Firefox(service=service, options=firefox_options)

    try:
        for row in phones_and_names_list[:-1]:
            row_list = row.split(",")
            phone = row_list[0].strip()
            name = row_list[1].strip()
            await send_message(driver, phone, name)
    finally:
        driver.quit()

    print("Все сообщения отправлены.")


if __name__ == "__main__":
    asyncio.run(main())
