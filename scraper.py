import requests
from bs4 import BeautifulSoup

def pobierz_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    }

    print(f"data downloading from:{url}...")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("data downloaded successfully")
        return response.text
    else:
        print(f'data download failed. status code:{response.status_code}')
        return None
    

html = pobierz_html("https://www.pracuj.pl/praca/intern-data-science;kw/wroclaw;wp")
print(html[:2000]) 