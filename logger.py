from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import json, os
from datetime import datetime
from os.path import exists
# add needed libraries

with open('login.json', 'r') as file:
    json_object = json.load(file)

username = json_object['username']
password = json_object['password']
private  = json_object['private']
# get account credentials from json file
# are we loging a private chat or a group chat?

if private == "Yes" or str.lower(private) == "true":
    private = True
elif private == "No" or str.lower(private) == "false":
    private = False
    
browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')
sleep(2)
# start browser and go to site

browser.find_element_by_css_selector("input[name='username']").send_keys(username)
browser.find_element_by_css_selector("input[name='password']").send_keys(password)
browser.find_element_by_xpath("//button[@type='submit']").click()
sleep(5)
# login 

browser.get('https://www.instagram.com/direct/inbox/')
sleep(2)
# go to dms

browser.find_element_by_css_selector("button.aOOlW:nth-child(2)").click()
sleep(2)
# close notification pop up

# browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a").click()
# sleep(2)
# # open first direct message chat

browser.find_element_by_xpath("//*[contains(text(), 'test')]").click()
sleep(2)
# open dms with a specific user

if exists('messages.txt') and (os.path.getsize('messages.txt') > 0):
    pass
else:
    open('messages.txt', "a+").writelines("##### LOG FILE " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " #####")
# if log file does not exist create it

while private:
    last_message = str(browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[last()]/div[2]/div").text)
    # get last message from site
    try:
        l_message_author = str(browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[last()]/div[1]/div/a").get_attribute("href"))[26:-1]
    except NoSuchElementException as exception:
        l_message_author = username
    # get last message's author if not found its probably you who sent it
    #! way slower than messages with an auther need fix
    last_line = ''
    with open('messages.txt', "r") as f:
        for line in f:
            pass
        last_line = line
        print(last_line)
        f.close()
        #get last entry from log file
    if last_message == last_line:
        pass
    else:
        with open('messages.txt', "a+") as f:
            f.writelines(datetime.now().strftime("\n%d/%m/%Y %H:%M:%S - ") + l_message_author + ':\n')
            f.writelines(last_message)
        f.close()
        # if last dm is already logged, do nothing, else log it

while not private: 
    last_message = str(browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[last()]/div[2]/div/div/div/div/div/div/div/div/span").text)
    # get last message from site
    # try:
    #     l_message_author = str(browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[last()]/div[1]/div/a").get_attribute("href"))[26:-1]
    # except NoSuchElementException as exception:
    #     l_message_author = username
    # except StaleElementReferenceException:
    #     sleep(0.5)
    #     l_message_author = str(browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[last()]/div[1]/div/a").get_attribute("href"))[26:-1]
    #TODO: idk how to get message author reliably
    last_line = ''
    with open('messages.txt', "r") as f:
        for line in f:
            pass
        last_line = line
        print(last_line)
        f.close()
        #get last entry from log file
    if last_message == last_line:
        pass
    else:
        with open('messages.txt', "a+") as f:
            f.writelines(datetime.now().strftime("\n%d/%m/%Y %H:%M:%S - ") + ':\n')
            f.writelines(last_message)
        f.close()
        # if last dm is already logged, do nothing, else log it
#? probably better to log to a json file or a db