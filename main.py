import requests
from bs4 import BeautifulSoup
from lxml import html
import pyfiglet

banner = pyfiglet.figlet_format('GOAT')
print(banner)
response = requests.get('https://www.goat.com/sneakers/air-jordan-1-retro-high-og-neutral-grey-dc1788-029/available-sizes')
print("status code: ", response.status_code)
print("\n")
print(response.headers)
print("\n")
print(response.cookies)
print("\n")
soup = BeautifulSoup(response.content, 'html.parser')
soup.find_all('div', class_='ProductVariantSize__Wrapper-ci5six-0 dCiSfE')
soup.find_all('div', class_='ProductVariantButtonPrice-fapubr-2 fHJrlz')
#tree = html.fromstring(response.content)
#sizes = tree.xpath('//*[@id="root"]/div[1]/div[4]/div[1]/div[2]/div/div[2]/div/a[1]/div[2]')
#prices = tree.xpath('//*[@id="root"]/div[1]/div[4]/div[1]/div[2]/div/div[2]/div/a[1]/div[3]')
#print('Sizes: ', sizes)
#print("\n")
#print('Prices: ', prices)