# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(8)

# Click on best sellers item
Best_sellers = driver.find_element("xpath", "/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[1]")
Best_sellers.click()

# Waiting for the search results page to load
time.sleep(5)

# Click on video games option
video_game = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[31]/a")
video_game.click()

time.sleep(2)
# Open video game
video_game1 = driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/div/a[1]/div/img")
video_game1.click()

# Waiting for the video game details page to load
time.sleep(2)

#Click on add gift option Check box
gift_wrap = driver.find_element("xpath", "/html/body/div[2]/div/div[5]/div[3]/div[1]/div[4]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/form/div/div/div/div/div[4]/div/div[42]/div/label/input")
gift_wrap.click()
time.sleep(2)
# Adding the Video game to the Wish list
add_to_wish_list = driver.find_element("id", "wishListMainButton")
add_to_wish_list.click()

# Waiting for the cart to update
time.sleep(3)


# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
