from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import json
from os.path import exists
# add needed libraries

with open('login.json', 'r') as file:
    json_object = json.load(file)

username = json_object['username']
password = json_object['password']
# get account credentials from json file

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

browser.find_element_by_css_selector("button.aOOlW:nth-child(2)") .click()
sleep(2)
# close notification pop up

browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a").click()
sleep(2)
# open first direct message chat

if exists('messages.txt'):
    pass
else:
    open('messages.txt', "a+").writelines("##### LOG FILE #####")
# if log file does not exist create it

while True:
    last_message =  str(browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[last()]/div[2]/div").text)
    # get last message from site
    try:
        l_message_author = str(browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[last()]/div[1]/div/a").get_attribute("href"))[26:-1]
    except NoSuchElementException as exception:
        l_message_author = username

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
            f.writelines('\n' + l_message_author + ':\n')
            f.writelines(last_message)
        f.close()
        # if last dm is already logged, do nothing, else log it
#? probably better to log to a json file