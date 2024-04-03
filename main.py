from bs4 import BeautifulSoup as B
import requests
import csv

URL = 'https://www.sulpak.kg/f/'

class Parser():
    def __init__(self,url:str,path:str) -> None:
        self.url = URL+url
        self.path = path

    def get_connect(self):
        request = requests.get(self.url)
        soup = B(request.content,'html.parser')
        items = soup.find_all('div', class_ = 'product__item product__item-js tile-container')
        new_list = []
        for i in items:
            new_list.append(
                {
                    'Title': i.find('div', class_ = 'product__item-name').find('a').get_text(strip = True),
                    'Price': i.find('div', class_ = 'product__item-price').get_text(strip = True),
                    'Img': i.find("div",class_="product__item-images-block").find('a').get('href')                    
            }
            )
        return new_list
    
    def save(self,products):
        with open(self.path, 'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['Название', 'Цена', 'Изображение'])
            for i in products:
                writer.writerow([i['Title'], i['Price'], i['Img']])
p = Parser(
    url = input("Введите категорию:"),
    path= "{}.csv".format(input("введите название файла:"))
)
a = p.get_connect()
p.save(a)
