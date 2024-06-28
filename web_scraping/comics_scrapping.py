#! python3
# downloadXkcd.py - Downloads the first 10 XKCD comics.

import requests, os, bs4

url = "https://xkcd.com"  # starting url
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd

comic_count = 0
while not url.endswith("#") and comic_count < 10:
    # Download the page.
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the URL of the comic image.
    comic_elem = soup.select("#comic img")
    if comic_elem:
        comic_url = "https:" + comic_elem[0].get("src")
        # Download the image.
        print(f"Downloading image {comic_url}...")
        res = requests.get(comic_url)
        res.raise_for_status()

        # Save the image to ./xkcd.
        image_file = open(os.path.join("xkcd", os.path.basename(comic_url)), "wb")
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

        comic_count += 1

    # Get the Prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prev_link.get("href")

print("Job's done.")
