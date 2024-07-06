# Unsplash Image Downloader

This script allows you to download images from Unsplash collections in batches. It uses Selenium for web scraping and requests for downloading images. The script handles downloading images in sessions, ensuring that the download limit is respected.

## Features

- Downloads images from Unsplash collections in batches of 10.
- Creates a subfolder for each collection to avoid overwriting images.
- Handles session management to respect download limits.
- Logs activities and errors for debugging purposes.

## Requirements

- Python 3.6 or higher
- ChromeDriver
- Selenium
- Requests

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/unsplash-image-downloader.git
   cd unsplash-image-downloader
   