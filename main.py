import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import pyfiglet

banner = pyfiglet.figlet_format('Sole Supremacy')
print(banner)

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path='./chromedriver')
driver.get("https://www.solesupremacy.com/products/air-jordan-1-retro-gs-court-purple-white")
print(driver.current_url)
print(driver.title)
print('\n')
price = int(driver.find_element_by_id('productPrice').text)/100
select = driver.find_element_by_id('productSelect-option-0')
all_options = select.find_elements_by_tag_name("option")
print('${pr}'.format(pr=price))
print('\n')
for option in all_options:
    print(option.get_attribute("value"))