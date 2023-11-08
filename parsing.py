import requests 
from bs4 import BeautifulSoup

# url = 'https://akipress.org/'
# respons = requests.get(url=url)
# # print(respons.text)
# soup = BeautifulSoup(respons.text, 'lxml')
# all_news = soup.find_all('a',class_ = 'newslink')
# # print(all_news)
# n = 0 
# for news in all_news:
#     n += 1
#     with open ('news.txt','a+', encoding='utf-8') as news_file:
#         news_file.write(f"{n}) {news.text}\n")
#     print(f'{n}.', news.text)

def parsing_sulpak():
    n = 0
    for i in range(1, 21):
        url = f'https://www.sulpak.kg/f/smartfoniy?page={i}'
        respons = requests.get(url=url)
        soup = BeautifulSoup(respons.text, 'lxml')
        # print(respons)
        smartfoniy = soup.find_all('div', class_='product__item-name')
        prices = soup.find_all('div', class_='product__item-price')
        # print(smartfoniy)

        for name, price in zip(smartfoniy,prices):
            n += 1
            current_price = "".join(price.text.split())
            print(n, name.text, price.text)
parsing_sulpak()