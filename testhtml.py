from bs4 import BeautifulSoup
import requests

def pobierz_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parsuj_oferty(html):
    soup = BeautifulSoup(html, "html.parser")
    
    # KROK 1: znajdź WSZYSTKIE kontenery ofert
    oferty = soup.find_all("a", class_="posting-list-item")    
    print(f"Znaleziono ofert: {len(oferty)}")
    
    # KROK 2: dla każdej oferty wyciągnij dane
    for oferta in oferty:
        tytul = oferta.find("h3", class_="posting-title__position ng-star-inserted")
        firma = oferta.find("h4", class_="company-name tw-mb-0")
        
        print(f"{tytul.text.strip()} | {firma.text.strip()}")

# URUCHOM
url = "https://nofluffjobs.com/pl/praca/data-science"
html = pobierz_html(url)
parsuj_oferty(html)