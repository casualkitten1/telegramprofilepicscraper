This Python script allows you to scrape and download profile pictures from Telegram users' profiles.
Features

    Scrapes Telegram profile pages and retrieves the profile picture.
    Automatically creates a folder for each username and saves the profile picture inside.
    Uses a fake user agent to mimic a mobile browser for requests.

Requirements

Make sure you have the following Python libraries installed:

    requests: for making HTTP requests.
    beautifulsoup4: for parsing HTML.
    fake_useragent: for generating fake user agents.

You can install them using pip:

pip install requests beautifulsoup4 fake_useragent

How to Use

    Replace the list of usernames in the script with the Telegram usernames you want to scrape.

    usernames = ['username1', 'username2', 'username3']  # Add actual usernames

    Run the script. The program will:
        Visit each Telegram profile.
        Extract the profile picture.
        Save the image in a folder named after the username (inside a telegram_pics directory).

Example

$ python tlgprofilepicscraper.py
Found image URL: https://some-image-link.com/image.jpg
Downloaded image: username1_profile_pic.jpg

Folder Structure

    telegram_pics/
        username1/
            username1_profile_pic.jpg
        username2/
            username2_profile_pic.jpg

Notes

    The script assumes the profile picture is in the image tag with the class tgme_page_photo_image. If Telegram changes their HTML structure, the script might need updates.
    If no profile picture is found, it will print a message saying so.
