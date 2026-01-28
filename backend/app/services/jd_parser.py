import requests
from bs4 import BeautifulSoup

def fetch_jd_text(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(separator=" ")
