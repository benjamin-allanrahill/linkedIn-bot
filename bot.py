from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from config import Config
import csv
from progress.bar import IncrementalBar


#launch URL
linkedInUrl = "http://linkedin.com/"
driver = webdriver.Chrome("./chromedriver")

def login():
    username, password = driver.find_element_by_id("session_key"), driver.find_element_by_id("session_password")
    username.send_keys(Config.username)
    password.send_keys(Config.password)

    driver.find_element_by_class_name("sign-in-form__submit-button").click()
    print("successfully logged in")

def loginV2():
    username, password = driver.find_element_by_name("session_key"), driver.find_element_by_name("session_password")
    username.send_keys(Config.username)
    password.send_keys(Config.password)

    driver.find_element_by_class_name("from__button--floating").click()
    print("successfully logged in")



def connect(url):

    driver.get(url)

    # print(personalizeMessage())
    message = personalizeMessage()

    # press connect button
    driver.find_element_by_class_name("pv-s-profile-actions--connect").click()

    # press add Note
    driver.find_element_by_class_name("mr1").click()

   

    sendMessage(message)

def sendMessage(message):
    textArea = driver.find_element_by_id("custom-message")

    # add message
    textArea.send_keys(message)

    # connect
    driver.find_element_by_class_name("artdeco-button--primary").click()

def personalizeMessage() -> str:

    name = driver.find_element_by_class_name("t-24").get_attribute("innerHTML").strip().split()

    message = f"""Hi {name[0]}, nice to meet you!

What’s your go-to doodle?
    
I saw that you're also in Product Buds! I'd love to connect and pick your brain about PM! Let me know if you're interested :)
Best,
Benjamin
"""

    return message



if __name__ == "__main__":
    # define the driver
    

    driver.get(linkedInUrl)
    try:
        login()
    except:
        driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        loginV2()

    with open('./Product Buds_ Networking - Networking.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for i in range(139):
            next(reader)

        
        for row in reader:
            try:
                connect(row[1])
                print(f"\nConnection request sent to {row[0]}")
                bar = IncrementalBar('Waiting...', max=65)
                for i in range(65):
                    time.sleep(1)
                    bar.next()
            except:
                print(f"\nThere was an error connecting with {row[0]}")

    