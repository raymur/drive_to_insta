import os

from drive_download import download_most_recent_drive_file
from selenium_insta import instagram_file_upload


if __name__ == "__main__":
    file_path = download_most_recent_drive_file()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    caption = "caption"
    instagram_file_upload(username, password, file_path, caption)