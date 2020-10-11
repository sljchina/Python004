from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    
    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)

    # browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    # 跳转到登陆页面
    # btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    # btm1.click()
    # time.sleep(5)

    # 输入账号密码
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('15967864701')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('87886922')
    time.sleep(5)
    # 点击登录按钮
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    # 破解登录验证，需要模拟鼠标点击，不知道该怎么搞

    # cookies = browser.get_cookies() # 获取cookies
    # print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:    
    browser.close()