from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import json

with open('login.json', 'r') as file:
    json_object = json.load(file)

username = json_object['username']
password = json_object['password']

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')
sleep(2)

browser.find_element_by_css_selector("input[name='username']").send_keys(username)
browser.find_element_by_css_selector("input[name='password']").send_keys(password)

browser.find_element_by_xpath("//button[@type='submit']").click()
print('login successful')
sleep(5)

browser.get('https://www.instagram.com/direct/inbox/')
sleep(2)

browser.find_element_by_css_selector("button.aOOlW:nth-child(2)") .click()
print("click on `not now` for notifications") 
sleep(2)

browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[3]/a").click()
print("open one of the dms")
sleep(2)

while True:
    increment_message = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[last()]/div[2]/div"
    try:    
        message = browser.find_element_by_xpath(increment_message).text
        print(message)
    except NoSuchElementException as exception:
        print("no message to display")
        #? error handling if a specifc element does not exist

# textfield = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
# textfield.send_keys("this message is sent through a selenium bot by Array in a Matrix™")
#? find textbox and types a message 

# browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
#? sends whatever message was in text field

# sleep(10) 

# browser.close()