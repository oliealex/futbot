import os
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

options = webdriver.ChromeOptions()


load_dotenv()

TIMER=20
SLEEP_TIMER=1

user = os.getenv("USER")
pw = os.getenv("PASSWORD")


def login(driver):
    driver.find_element_by_xpath("//*[@id=\"Login\"]/div/div/button[1]").click()
    
    username = driver.find_element_by_xpath("//*[@id=\"email\"]")
    username.clear()
    username.send_keys(user)

    password = driver.find_element_by_xpath("//*[@id=\"password\"]")
    password.clear
    password.send_keys(pw)

 

    login = driver.find_element_by_xpath("//*[@id=\"btnLogin\"]/span")
    login.click()

def search_player(driver):
    WebDriverWait(driver, TIMER).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/nav/button[3]")))
    go_to_transfer = driver.find_element_by_xpath("/html/body/main/section/nav/button[3]")
    go_to_transfer.click()

    WebDriverWait(driver, TIMER).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/section/div[2]/div/div/div[2]")))
    go_to_search = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[2]")
    go_to_search.click()

    WebDriverWait(driver, TIMER).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input")))
    type_player_name = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input")
    type_player_name.send_keys("timo werner")

    time.sleep(SLEEP_TIMER)
    click_player = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/button")
    click_player.click()

    search = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")
    search.click()

    time.sleep(1)

def scan_player(driver):

    cur_price = 0;
    lower_price = 0
    search = True

    while search:
        time.sleep(1)

        check_prices = driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[3]/span[2]")

        if len(check_prices) > 0:
            search = True
            get_price = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[3]/span[2]")
            cur_price = float(get_price.text.replace(',',''))
            lower_price = cur_price - (cur_price * 0.01)

            go_back = driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]")
            go_back.click()

            WebDriverWait(driver, TIMER).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input")))
            fill_price = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input")
            fill_price.clear()
            fill_price.send_keys(str(lower_price))

            search = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")
            search.click()
        else:
            go_back = driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]")
            go_back.click()
            search = False

    time.sleep(5)

    return lower_price

def find_target(driver, price):
    target_price = price * 0.90

    print(target_price)
    WebDriverWait(driver, TIMER).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input")))
    fill_price = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input")
    fill_price.clear()
    fill_price.send_keys(str(target_price))

    search = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")
    search.click()

    time.sleep(1)
    check_prices = driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[3]/span[2]")
    print(len(check_prices))
    if len(check_prices) > 0:
        buy_and_list(driver)

    go_back = driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]")
    go_back.click()

def buy_and_list(driver):
    click_buy_player = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]")
    click_buy_player.click()

    WebDriverWait(driver, TIMER).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/section/div/div/button[1]")))
    buy_player = driver.find_element_by_xpath("/html/body/div[4]/section/div/div/button[1]")
    buy_player.click()

    time.sleep(10)
    

def signout(driver):
    WebDriverWait(driver, TIMER).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/nav/button[9]/span")))

    go_to_settings = driver.find_element_by_xpath("/html/body/main/section/nav/button[9]/span")
    go_to_settings.click()

    time.sleep(SLEEP_TIMER)
    WebDriverWait(driver, TIMER).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/section/div[2]/div/div/div[2]/div[1]/button[3]")))

    click_signout = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[2]/div[1]/button[3]")
    click_signout.click()

    time.sleep(SLEEP_TIMER)
    
    signout = driver.find_element_by_xpath("/html/body/div[4]/section/div/div/button[1]")
    signout.click()
    WebDriverWait(driver, TIMER).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/section/div/div/button[1]")))



def main():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\Alexa\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    driver =  webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.maximize_window()
    driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")

    time.sleep(15)
    find_target_buy = True
    i = 0

    check_login = driver.find_elements_by_xpath("//*[@id=\"Login\"]/div/div/button[1]")

    if len(check_login) > 0:
        login(driver)
    search_player(driver)
    price = scan_player(driver)

    while i < 1000:
        print(i)
        find_target(driver, price)
        i = i + 1

    signout(driver)

if __name__ == "__main__":
    main()