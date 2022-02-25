# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:12:25 2022

@author: tgoet
"""


##############################################################################
# imports
##############################################################################
import os
from os import chdir, getcwd
import os
from time import sleep 
import random
# https://pypi.org/project/flatten-dict/
from flatten_dict import flatten
from flatten_dict.reducers import make_reducer

from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver

from selenium.webdriver.common.by import By
from requests_html import HTMLSession
session = HTMLSession()

from progressbar import ProgressBar
import warnings
import pandas as pd
from tqdm import tqdm
tqdm.pandas()
wd = getcwd()  # lets you navigate using chdir within jupyter/spyder
chdir(wd)
warnings.simplefilter(action='ignore', category=FutureWarning)
pbar = ProgressBar()




# set directory to where this file is located
folder_loc = os.path.dirname(os.path.realpath(__file__))
os.chdir(folder_loc)




url = 'https://www.chickenderby.com/result'
bot_path = 'C:/Users/tgoet/Documents/GitHub/chromedriver.exe'




# check if an element exists
def hasXpath(bot, xpath):
    try:
        # check xpath first
        bot.find_element_by_xpath(xpath)
        return True
    except:
        try:
            # check if css selector was entered instead
            bot.find_element_by_css_selector(xpath)
            return True
        except:
            return False


def sleep_for(opt1, opt2):
    time_for = random.uniform(opt1, opt2)
    time_for_int = int(round(time_for))
    sleep(abs(time_for_int - time_for))
    for i in range(time_for_int, 0, -1):
        # sys.stdout.write(str(i) + ' ')
        # sys.stdout.flush()
        sleep(1)


def initialize_bot():
    chrome_options = Options()
    chrome_options.add_argument('--disable-background-timer-throttling')
    chrome_options.add_argument('--disable-backgrounding-occluded-windows')
    chrome_options.add_argument('--disable-background-timer-throttling')
    chrome_options.add_argument('--disable-renderer-backgrounding')
    chrome_options.add_argument('detach:True')
    # add metamask
    # chrome_options.add_extension('resources/MetaMask.crx')
    # chrome_options.add_argument('--headless') # run this line if you want pop up window
    return webdriver.Chrome(executable_path='C:/Users/tgoet/Documents/GitHub/chromedriver.exe', chrome_options=chrome_options)



# =============================================================================
# # first we want to get the proper headers to access the page
# =============================================================================
driver = initialize_bot()
sleep_for(5,10)
driver.maximize_window()


# switch to chicken derby site not metamask tab popup
tabs_open = driver.window_handles
driver.switch_to.window(tabs_open[1])


driver.get('https://www.npr.org/')

ps = driver.find_elements(By.XPATH, '//div[@class="story-text"]//a')
ps_text = [x.get_attribute('href') for x in ps]


ps[0].click()


# get cookies
# cookies_path = 'resources/cookies.json'

# cookies are not needed -- chickenderby site just wants to know that you have metamask extension installed
# doesn't need to be logged in


# uncomment one of the following to save or load cookies
# save cookies
# cookies = driver.get_cookies()
# with open(cookies_path, 'w', newline='') as outputdata:
#     json.dump(cookies, outputdata)
# print('cookies created')


# # add the account cookies
# with open( cookies_path , 'r', newline='') as inputdata:
#     cookies = json.load(inputdata)
# for i in cookies:
#     driver.add_cookie(i)
# sleep_for(1, 2)
# driver.get(url)
# sleep_for(4, 6)


sleep_for(5, 10)
driver.get(url)
sleep_for(15, 20)

user_agent = driver.execute_script("return navigator.userAgent;")
