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

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
Best_sellers = driver.find_element("xpath", "/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[1]")
Best_sellers.click()

# Submitting the search query
#Best_sellers.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
#assert "laptop" in driver.title

# Selecting a laptop from the search results
video_game = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[31]/a")
video_game.click()

time.sleep(2)
video_game1 = driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/div/a[1]/div/img")
video_game1.click()

# Waiting for the laptop details page to load
time.sleep(2)

#Switch_Digital_Code = driver.find_element("xpath", "/html/body/div[2]/div/div[5]/div[3]/div[4]/div[28]/div[1]/div/form/div[1]/ul/li[3]/span/div/span/span/span/button/div/div[1]/p")
#Switch_Digital_Code.click()
#time.sleep(2)
#Booster_Course_Pass = driver.find_element("xpath", "/html/body/div[2]/div/div[5]/div[3]/div[4]/div[28]/div[1]/div/form/div[1]/ul/li[3]/span/div/span/span/span/button/div/div[1]/p")
#Booster_Course_Pass.click()
#time.sleep(2)
gift_wrap = driver.find_element("xpath", "/html/body/div[2]/div/div[5]/div[3]/div[1]/div[4]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/form/div/div/div/div/div[4]/div/div[42]/div/label/input")
gift_wrap.click()
time.sleep(2)
# Adding the laptop to the cart
add_to_wish_list = driver.find_element("id", "wishListMainButton")
add_to_wish_list.click()

# Waiting for the cart to update
time.sleep(5)

# Clicking on no thanks button
# no_thanks_button= driver.find_element("xpath","/html/body/div[9]/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/span[2]/span/input")
# no_thanks_button.click()Y
# time.sleep(2)

#proceed_to_checkout= driver.find_element("xpath", "/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/form/span/span/span/input")
#proceed_to_checkout.click()
#time.sleep(2)


# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
