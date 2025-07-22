import requests
from bs4 import BeautifulSoup as BS
import xlsxwriter



page = 1

rek = ('https://xn--80aaig9ahr.xn--c1avg')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
data = [['Name', 'title']]


def get_sol(url):
   res1 = requests.get(url, headers)
   return BS(res1.text, 'html.parser')



while True:
    res = requests.get("https://xn--80aaig9ahr.xn--c1avg/manga?page=" + str(page),
                       "&content=manga&categories=63&count_chapters_gte=20&count_chapters_lte=5000")
    soup = BS(res.text, 'html.parser')
    headlines = soup.find_all('a', class_='Vertical_card__Qez7E')


    if(len(headlines)):
        for cat in headlines:
            a = cat.find_all('a', class_='Vertical_card__Qez7E')
            name = cat['title'].strip()
            subcategories = get_sol(rek + cat['href'])
            manga_items = subcategories.find_all('div', class_='Typography_body1__YTqxB')
            print(name)

            for manga in manga_items:
                title = manga.text.strip()
                data.append([name, title])

        page += 1
    else:
        break

with xlsxwriter.Workbook('manga.xlsx') as w:
    worksheet = w.add_worksheet()

    for row_num, info in enumerate(data):
        worksheet.write_row(row_num, 0, info)

