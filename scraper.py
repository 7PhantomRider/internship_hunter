from bs4 import BeautifulSoup
import requests
import pandas as pd

def pobierz_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parsuj_oferty(html):

    lista_ofert = []
    
    soup = BeautifulSoup(html, "html.parser")
    
    oferty = soup.find_all("a", class_="posting-list-item")
    print(f"Znaleziono ofert: {len(oferty)}")
    
    for oferta in oferty:
  
        element_h3 = oferta.find("h3", class_="posting-title__position")
        firma = oferta.find("h4", class_="company-name tw-mb-0")
        tytul = wyczysc_tytul(element_h3) if element_h3 is not None else "Brak tytułu"
        lokalizacja = oferta.find("nfj-posting-item-city", {"data-cy": "location on the job offer listing"})
        
        firma_text = firma.text.strip() if firma is not None else "Brak firmy"
        lokalizacja_text = lokalizacja.text.strip() if lokalizacja is not None else "Brak lokalizacji"

        
        #print(f"{tytul} | {firma_text.strip()} | {lokalizacja_text.strip()}")

        lista_ofert.append({
            "tytul": tytul,
            "firma": firma_text,
            "lokalizacja": lokalizacja_text
        })

    return pd.DataFrame(lista_ofert)



def wyczysc_tytul(element_h3):
    odznaka = element_h3.find("span", class_="title-badge")
    if odznaka:
        odznaka.decompose()
    return element_h3.text.strip()

url = "https://nofluffjobs.com/pl/praca/data-science"
html = pobierz_html(url)
df = parsuj_oferty(html)
print(df)
#parsuj_oferty(html)