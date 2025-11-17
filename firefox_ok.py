from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 启动浏览器
driver = webdriver.Firefox()

try:
    driver.get("https://www.baidu.com")
    
    # 显式等待：等待搜索框加载完成（最多等10秒）
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "kw"))  # 按ID定位搜索框
    )
    
    # 交互操作：输入内容+点击搜索
    search_input.send_keys("Python Selenium Firefox")  # 输入搜索词
    driver.find_element(By.ID, "su").click()  # 点击搜索按钮
    
    time.sleep(3)  # 观察搜索结果

finally:
    driver.quit()
