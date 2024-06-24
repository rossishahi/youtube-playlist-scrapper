from selenium import webdriver
from selenium.webdriver.common.by import By
import requests, lxml, bs4

def playlist_selection():
    playlist_url = ''
    
    while 'playlist' not in playlist_url:
        playlist_url = input("Enter playlist URL.")

        if 'playlist' not in playlist_url:
            print("\nURL entered is not a playlist. Please try again.")
            continue
        else:
            break
    return playlist_url

def action_selection():
    #providing the options for available scrapping actions
    print("\nYou can proceed further. Please select the relevant action to be performed.")

    options = {1: 'Identify playlist title.', 2:'Identify the title of the videos in the playlist.',\
    3:'Identify the title of the videos in the playlist along with their urls.'}

    for num in options:
        print(f'{num}. {options[num]}')

    action = 0
    
    while action not in options:
        try:
            action = int(input("\nEnter the number for the action to be performed."))

        except:
            print("\nEntered input is invalid. Please try again.")
            break

    return action

def title_scrapper(playlist_url):
    request = requests.get(playlist_url)
    soup = bs4.BeautifulSoup(request.text, 'lxml')

    title = soup.select('title')[0].text.split(' - ')[0]

    print(f'Playlist Title: {title}')

def playlist_scrapper(playlist_url):
    # Initialize WebDriver
    driver = webdriver.Chrome()

    # Open the playlist URL
    playlist_url = 'https://www.youtube.com/playlist?list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF'
    driver.get(playlist_url)

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Find all video elements
    videos = driver.find_elements(By.CSS_SELECTOR, 'a#video-title')

    if videos == []:
        print("\nNo relevant links found.")

    else:
    # Iterate through videos and print title and URL
        video_list = []
        for num, video in enumerate(videos):
            title = video.get_attribute('title')
            url = video.get_attribute('href')
            print(f'{num+1}. {title}')
            video_list.append((title, url))

if __name__ == '__main__':

        scrapper_on = True
        playlist_url = playlist_selection()

        while scrapper_on:
            
            action = action_selection()

            if action == 1:
                title_scrapper(playlist_url)
            elif action == 2:
                playlist_scrapper(playlist_url)
            elif action == 3:
                pass

            continue_scrapping = ''

            while continue_scrapping.lower() not in ['y', 'n']:
                continue_scrapping = input("\nDo you want to continue scrapping? Enter 'Y' or 'N'.")

                if continue_scrapping.lower() not in ['y', 'n']:
                    print("\nInvalid input. Please try again.")
                    continue

                else:
                    if continue_scrapping == 'y':
                        scrapper_on = True
                        print("\nOkay. Please continue with the other scrapping options.")
                        break

                    elif continue_scrapping == 'n':
                        scrapper_on = False
                        print("\nThank you for using this scrapper. Hope to see you again.")
                        break










