import requests
from bs4 import BeautifulSoup

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
soup = BeautifulSoup(response.text, features='html.parser')

usd = soup.find(text="USD").find_parent("tr").find("td", {"data-label": "Офіційний курс"}).text
print(usd)