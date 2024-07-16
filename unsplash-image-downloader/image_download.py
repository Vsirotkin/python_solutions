# BEFORE CODE-REVIEW
#
#
# import os
# import time
# import requests
# import logging
# from pathlib import Path
# from urllib.parse import urlparse
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import (
#     StaleElementReferenceException,
#     NoSuchElementException,
#     InvalidArgumentException,
# )

# # Configure logging
# logging.basicConfig(
#     filename="script.log",
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )


# def download_image(image_url, save_path):
#     try:
#         response = requests.get(image_url, stream=True)
#         response.raise_for_status()  # Raise an exception for HTTP errors

#         with open(save_path, "wb") as file:
#             for chunk in response.iter_content(1024):
#                 file.write(chunk)
#         print(f"Downloaded: {save_path}")
#         logging.info(f"Downloaded: {save_path}")

#     except requests.exceptions.RequestException as e:
#         print(f"Error downloading image: {e}")
#         logging.error(f"Error downloading image: {e}")


# def get_image_urls(collection_url, num_images):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run in headless mode
#     service = Service(
#         "/usr/bin/chromedriver"
#     )  # Update with the path to your ChromeDriver
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     try:
#         driver.get(collection_url)
#         logging.info(f"Navigated to: {collection_url}")
#     except InvalidArgumentException as e:
#         print(f"Invalid URL: {collection_url}")
#         logging.error(f"Invalid URL: {collection_url}")
#         driver.quit()
#         return []

#     # Save the HTML of the page for inspection
#     with open("page.html", "w", encoding="utf-8") as file:
#         file.write(driver.page_source)
#     logging.info("Saved page HTML to page.html")

#     # Wait for the images to load (you might need to adjust the wait time)
#     driver.implicitly_wait(20)
#     logging.info("Waiting for images to load...")

#     # Click the "Load more" button until the desired number of images is loaded
#     while (
#         len(
#             driver.find_elements(
#                 By.CSS_SELECTOR, "img[src*='https://plus.unsplash.com/premium_photo-']"
#             )
#         )
#         < num_images
#     ):
#         try:
#             load_more_button = driver.find_element(
#                 By.XPATH, "//button[text()='Load more']"
#             )
#             logging.info('Found "Load more" button')
#             driver.execute_script("arguments[0].click();", load_more_button)
#             logging.info('Clicked "Load more" button')
#             time.sleep(5)  # Wait for new images to load
#         except NoSuchElementException:
#             logging.warning('"Load more" button not found')
#             break

#     image_urls = []
#     retries = 3
#     for _ in range(retries):
#         try:
#             # Extract image URLs using CSS_SELECTOR
#             image_elements = driver.find_elements(
#                 By.CSS_SELECTOR, "img[src*='https://plus.unsplash.com/premium_photo-']"
#             )
#             image_urls = [
#                 img.get_attribute("src") for img in image_elements[:num_images]
#             ]
#             logging.info(f"Found {len(image_urls)} image URLs")
#             break
#         except StaleElementReferenceException:
#             logging.warning("Stale element reference. Retrying...")
#             continue

#     driver.quit()
#     return image_urls


# def main():
#     collection_counter = 1
#     while True:
#         collection_url = input("Enter the URL of the Unsplash collection: ").strip()
#         num_images = int(input("Enter the number of images you want to download: "))

#         # Validate the URL
#         parsed_url = urlparse(collection_url)
#         if not all([parsed_url.scheme, parsed_url.netloc]):
#             print("Invalid URL. Please enter a valid URL.")
#             logging.error("Invalid URL. Please enter a valid URL.")
#             continue

#         save_dir = Path("images") / str(collection_counter)
#         save_dir.mkdir(parents=True, exist_ok=True)

#         image_urls = get_image_urls(collection_url, num_images)

#         for start in range(0, num_images, 10):
#             end = min(start + 10, num_images)

#             for i, image_url in enumerate(image_urls[start:end], start=1):
#                 save_path = save_dir / f"image_{start + i}.jpg"
#                 download_image(image_url, save_path)

#         collection_counter += 1

#         if (
#             input(
#                 "Do you want to download images from another collection? (yes/no): "
#             ).lower()
#             != "yes"
#         ):
#             break


# if __name__ == "__main__":
#     main()


# AFTER CODE-REVIEW
import os
import time
import requests
import logging
from pathlib import Path
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
    InvalidArgumentException,
)

logging.basicConfig(
    filename="script.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

IMAGE_CHUNK_SIZE = 10
WAIT_TIME = 20


def download_image(image_url, save_path):
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        logging.info(f"Downloaded: {save_path}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error downloading image: {e}")


def get_image_urls(driver, collection_url, num_images):
    try:
        driver.get(collection_url)
        logging.info(f"Navigated to: {collection_url}")
    except InvalidArgumentException as e:
        logging.error(f"Invalid URL: {collection_url}")
        return []

    with open("page.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    logging.info("Saved page HTML to page.html")

    driver.implicitly_wait(WAIT_TIME)
    logging.info("Waiting for images to load...")

    while (
        len(
            driver.find_elements(
                By.CSS_SELECTOR, "img[src*='https://plus.unsplash.com/premium_photo-']"
            )
        )
        < num_images
    ):
        try:
            load_more_button = driver.find_element(
                By.XPATH, "//button[text()='Load more']"
            )
            logging.info('Found "Load more" button')
            driver.execute_script("arguments[0].click();", load_more_button)
            logging.info('Clicked "Load more" button')
            time.sleep(5)  # Wait for new images to load
        except NoSuchElementException:
            logging.warning('"Load more" button not found')
            break

    image_urls = []
    retries = 3
    for _ in range(retries):
        try:
            image_elements = driver.find_elements(
                By.CSS_SELECTOR, "img[src*='https://plus.unsplash.com/premium_photo-']"
            )
            image_urls = [
                img.get_attribute("src") for img in image_elements[:num_images]
            ]
            logging.info(f"Found {len(image_urls)} image URLs")
            break
        except StaleElementReferenceException:
            logging.warning("Stale element reference. Retrying...")
            continue

    return image_urls


def main():
    collection_counter = 1
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    service = Service(
        "/usr/bin/chromedriver"
    )  # Update with the path to your ChromeDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    while True:
        collection_url = input("Enter the URL of the Unsplash collection: ").strip()
        num_images = int(input("Enter the number of images you want to download: "))

        parsed_url = urlparse(collection_url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            print("Invalid URL. Please enter a valid URL.")
            logging.error("Invalid URL. Please enter a valid URL.")
            continue

        save_dir = Path("images") / str(collection_counter)
        save_dir.mkdir(parents=True, exist_ok=True)

        image_urls = get_image_urls(driver, collection_url, num_images)

        for start in range(0, num_images, IMAGE_CHUNK_SIZE):
            end = min(start + IMAGE_CHUNK_SIZE, num_images)

            for i, image_url in enumerate(image_urls[start:end], start=1):
                save_path = save_dir / f"image_{start + i}.jpg"
                download_image(image_url, save_path)

        collection_counter += 1

        if (
            input(
                "Do you want to download images from another collection? (yes/no): "
            ).lower()
            != "yes"
        ):
            break

    driver.quit()


if __name__ == "__main__":
    main()
