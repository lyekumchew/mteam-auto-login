import sys
import time
from selenium import webdriver


def login():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://pt.m-team.cc/login.php")
    username_box = driver.find_element_by_name("username")
    username_box.send_keys(username)
    passwd_box = driver.find_element_by_name("password")
    passwd_box.send_keys(password)
    driver.find_element_by_class_name("btn").click()
    time.sleep(1)
    driver.get("https://pt.m-team.cc/bet.php")
    time.sleep(1)
    html = driver.page_source

    if html.__contains__("該頁面必須在登錄後才能訪問"):
        print("登录失败")
        exit(1)
    else:
        if html.__contains__(username):
            print("登录成功")
            exit(0)
        else:
            print("登录失败")
            exit(1)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    login()
