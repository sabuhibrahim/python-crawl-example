import random
import bs4
import requests


# Fake UserAgent List
BROWSERS = {
    'chrome': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'opera': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.31',
    'edge': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    'firefox': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
}



def find_price(url, keyword='price', element=None, attr='class'):
    browser = BROWSERS[random.choice(list(BROWSERS))] # Random selection from the above BROWSERS
    response = requests.get(url, headers={
        'User-Agent': browser
    })

    if response.status_code not in [200, 201]:
        print(f"status={response.status_code} | url = {url}")
        return None
    
    content = response.content.decode('utf-8')
    soup = bs4.BeautifulSoup(content, "html.parser")
    if element:
        elements = soup.find_all(element, attrs={attr: keyword})
    else:
        elements = soup.find_all(attrs={attr: keyword})
    prices = [e.get_text() for e in elements]
    return prices or None
