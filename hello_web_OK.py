from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from base.util import *


def open_webpage(url):
    logger.info(f"初始化Chrome浏览器驱动: {url}")
    # 初始化Chrome浏览器驱动
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # 打开指定网页
        driver.get(url)
        logger.info(f"成功打开网页: {url}")

        # 找到用户名和密码的输入框
        username_box = driver.find_elements(By.ID, "username")  # 假设用户名输入框的ID是'username'
        logger.info(f'username_box:{username_box}')

        password_box = driver.find_elements(By.ID, "password")  # 假设密码输入框的ID是'password'
        logger.info(f'password_box:{password_box}')

        # 输入用户名和密码
        username_box[0].send_keys(f'CUSTOM@120')
        password_box[0].send_keys(f'qweqwe')

        time.sleep(3)

        # 找到登录按钮并点击
        login_button = driver.find_element(By.ID, "login")
        logger.info(f'login_button:{login_button}')
        login_button.click()

        time.sleep(3)

        # second page
        # /html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/i
        links = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/i')
        logger.info(f'links:{links}')
        links.click()

        #
        id = '/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div/div'
        time.sleep(3)
        links = driver.find_element(By.XPATH, id)
        logger.info(f'links:{links}')
        links.click()

        #溯源
        id = '/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[4]/div/div/span'
        time.sleep(3)
        links = driver.find_element(By.XPATH, id)
        logger.info(f'links:{links}')
        links.click()

        # 碳中和
        id = '/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[6]/div/div'
        time.sleep(3)
        links = driver.find_element(By.XPATH, id)
        logger.info(f'links:{links}')
        links.click()

        # 停留5秒，让用户有时间查看
        time.sleep(600)

    except Exception as e:
        logger.info(f"打开网页时发生错误: {e}")

    finally:
        # 关闭浏览器
        driver.quit()
        logger.info("浏览器已关闭")


if __name__ == "__main__":
    # 要打开的网页URL
    target_url = "https://routinecloud.sciento.cn/login"  # 可以替换为任何想要打开的网页
    open_webpage(target_url)
