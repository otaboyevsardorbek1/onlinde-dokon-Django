from pprint import pprint

import requests
import bs4
import json

# # response = requests.get('https://www.instagram.com/')
# response = requests.get('https://www.gazeta.ru/')
# print(response.text)
def scrapping_gazeta_ru(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    blocks = soup.select('.b_ear:not(.m_titleonly).b_ear:not(.m_simple).b_ear:not(.m_line).b_ear:not(.m_outline2)')
    data_news = []
    for block in blocks:
        title = block.select_one('.b_ear-title > a').get_text().strip().replace(' ', ' ')
        link = 'https://www.gazeta.ru' + block.select_one('.b_ear-title > a')['href']
        desc = block.select_one('.b_ear-intro')
        img = block.select_one('img')['src']
        if desc:
            desc = block.select_one('.b_ear-intro > a').get_text().strip().replace(' ', ' ')
        else:
            desc = "Нет описания"

        data_news.append({
            'id': blocks.index(block) + 1,
            'title': title,
            'link': link,
            'desc': desc,
            'img': img
        })

    with open('GazeteRU.json', mode='w', encoding='utf-8') as file:
        json.dump(data_news, file, indent=4, ensure_ascii=False)
scrapping_gazeta_ru('https://www.gazeta.ru/')