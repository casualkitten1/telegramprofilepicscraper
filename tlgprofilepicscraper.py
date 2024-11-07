import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Function to create the folder if it doesn't exist
def create_folder(username):
    folder_path = f"telegram_pics/{username}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

# Function to download the image
def download_image(img_url, folder_path, img_name):
    try:
        img_data = requests.get(img_url).content
        img_path = os.path.join(folder_path, img_name)
        with open(img_path, 'wb') as file:
            file.write(img_data)
        print(f"Downloaded image: {img_name}")
    except Exception as e:
        print(f"Error downloading {img_name}: {e}")

# Function to scrape the Telegram profile
def scrape_telegram_profile(username):
    ua = UserAgent()
    headers = {
        'User-Agent': ua.safari,  # Fake Safari mobile user agent
        'Referer': 'https://www.google.com',  # Fake Google referrer
    }

    # Construct the URL of the user's Telegram profile
    url = f"https://t.me/{username}"

    try:
        # Send the request to the profile
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the image URL using the specified class
        img_tag = soup.find('img', class_='tgme_page_photo_image')
        
        if img_tag:
            img_url = img_tag['src']
            print(f"Found image URL: {img_url}")

            # Create the folder and download the image
            folder_path = create_folder(username)
            img_name = f"{username}_profile_pic.jpg"
            download_image(img_url, folder_path, img_name)
        else:
            print(f"No profile picture found for {username}.")
    except requests.exceptions.RequestException as e:
        print(f"Error scraping profile {username}: {e}")

# List of Telegram usernames to scrape
usernames = ['x', 'x', 'x']  # Replace with actual usernames

# Loop through the usernames and scrape their profiles
for username in usernames:
    scrape_telegram_profile(username)
