import getpass
import random
import string
import time

from selenium import webdriver
from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException,
                                        TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options


def page_loaded(browser):
    return browser.find_element_by_tag_name('body') != None

def input_data(element, data):
    return element.send_keys(data)


#Nzubepostbot 419 text generator
first_word = random.choice(string.ascii_uppercase) + "".join([random.choice(string.ascii_lowercase) for i in range(random.randint(10, random.randint(15, 30)))])

emoji_chance = 100
threemoji_chance = 15
symbol_chance = 30
actual_word_chance = 5

emojis = ['😂', '👌', '😂', '💀', '💋', '💩']
threemojis = ['👫💯💵', '🍔🍖🐹']
symbols = ['? ', '_', '-', '/', ':', '@', '8']
actual_words = ['watchwhatyousay ', ' Hamayel', 'EA', 'FAg', ' eye why']

def new_word():
    n_word = " " + ''.join([random.choice(string.ascii_lowercase) for i in range(random.randint(2, (random.randint(3, 30))))])
    return n_word

def gen_rand_words():
    word_list = []
    for i in range(random.randint(0, random.randint(2, 8))):
        word_list.append(new_word())
    return word_list

def create_sentence():
    sentence = ''
    edited_list = gen_rand_words()
    final_list = []
    chance = random.randint(1, 101)
    if chance <= emoji_chance or chance <= threemoji_chance or chance <= symbol_chance or chance <= actual_word_chance:
        if chance <= emoji_chance:
            edited_list.append(random.choice(emojis))
        if chance <= threemoji_chance:
            edited_list.append(random.choice(threemojis))
        if chance <= symbol_chance:
            edited_list.append(random.choice(symbols))
        if chance <= actual_word_chance:
            edited_list.append(random.choice(actual_words))
        for i in range(len(edited_list)):
            rand_el = edited_list.index(random.choice(edited_list))
            final_list.append(edited_list.pop(rand_el))
        sentence = first_word + "".join(final_list)
    else:
        sentence = first_word + "".join(gen_rand_words())
    return sentence


#Getting your login details to post to Nzubepostbot 419 demo
input_email_id = "YOUR EMAIL HERE"
input_pwd = "YOUR PASSWORD HERE"


#Setting up the browser options so that Chrome pop ups are blocked and the browser runs in headless mode (background)
print("Running Script")
browser_options = Options()
browser_options.headless = True
browser_options.set_preference("dom.webnotifications.enabled", False)


#Setting up the browser driver and loading up the first page
browser = webdriver.Firefox(options=browser_options, executable_path=r'C:\\Users\\Hamayel\\Desktop\\webdrivers\\geckodriver.exe')
browser.get("https://www.facebook.com/DESIREDLINKHERE/")
print("Page Loading...")
wait = ui.WebDriverWait(browser, 3)
wait.until(page_loaded)
print("Page Loaded")


#Finding the email and password fields on the login page
email = browser.find_element_by_id('email')
password = browser.find_element_by_id('pass')
login_button = browser.find_element_by_xpath('//*[@id="loginbutton"]')


#Sending the login information
input_data(email, input_email_id)
input_data(password, input_pwd)
time.sleep(2)
login_button.click()
# password.send_keys(Keys.RETURN) For some reason this does not work on the firefox driver
print("Login Information Sent...")


#After succesfully logging into my facebook wall, switching over to the facebook page on which I want to post
print("Page Loading...")
browser.get("https://www.facebook.com/FACEBOOKPAGE/")
print("Page Loaded")


#xpath for the text box in which we must enter our generated text
xpath = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div'


#This part takes care of posting the randomly generated string to the facebook page
try:
    post_box = browser.find_element_by_class_name('_3nd0')
    post_box.click()
    print("Box Open...")
    time.sleep(2)
    try:
        text_box = browser.find_element_by_xpath(xpath)
        text_box.click()
        print("Text Box Found")
        time.sleep(5)
        try:
            text_box.send_keys(Keys.HOME)
            input_data(text_box, create_sentence())
            # text_box.send_keys(sentence)
            print("Words Entered!")
            try:
                submit_button = browser.find_element_by_xpath('//*[@id="composerPostButton"]/div/button')
                submit_button.click()
                time.sleep(2)
                print("Post made")
            except NoSuchElementException:
                print("Where's the button?")
        except ElementNotInteractableException:
            print("Cannot interact with this element")
    except NoSuchElementException:
        print("that's not the text box")
except NoSuchElementException:
    print("Cannot find the post box element")


#Post complete, closing the browser after 6 seconds
time.sleep(6)
print("Closing browser window")
browser.close()
