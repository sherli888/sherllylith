from selenium import webdriver

profile_dir = r'C:\Users\sherli\AppData\Roaming\Mozilla\Firefox\Profiles\n8l3abda.default-release'
profile = webdriver.FirefoxProfile(profile_dir)
# 启动浏览器配置
#driver = webdriver.Firefox(profile)
driver = webdriver.Firefox()

driver.get('http://www.baidu.com/')
input = driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('su').click()

