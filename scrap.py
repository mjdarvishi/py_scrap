import requests
from bs4 import BeautifulSoup
import openpyxl

#prepration for writing in excell file
filename = 'b:\\python\\sample.xlsx'
wb = openpyxl.load_workbook(filename=filename)
sheet = wb['Sheet1']
# fech 500 page 
for x in range(500):
    # getting page HTML
    page = requests.get(f'https://divar.ir/s/tehran/auto?page={x}')
    # parsing content using beautifulsoup
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.select("div .post-card-item")
    for idx, item in enumerate(links):
        details = item.select(
            'div .kt-post-card__description')[0].text.split('\n')
        new_row = [item.select('div .kt-post-card__title')[0].text,
                   details[1] if len(details) > 1 else 0, details[0],(item.select('a', href=True)[0]['href']).split('/')[-1]]
        sheet.append(new_row)
    print(f'page {x} has been completed')   
    wb.save(filename)
