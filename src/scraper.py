import requests
from bs4 import BeautifulSoup
import json

class WikipediaScraper:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        self.cookie = self.refresh_cookie()

    def refresh_cookie(self):
        cookie_url = self.base_url + self.cookies_endpoint
        cookie_response = requests.get(cookie_url)
        cookie = cookie_response.cookies.get('user_cookie')
        return cookie
   
    def get_countries(self):
        countries_url = self.base_url + self.country_endpoint
        response = requests.get(countries_url, cookies={'user_cookie': self.cookie})
        countries = response.json()
        return countries

    def get_leaders(self, country):
        leaders_url = f"{self.base_url}{self.leaders_endpoint}?country={country}"
        response = requests.get(leaders_url, cookies={'user_cookie': self.cookie})
        self.leaders_data[country] = response.json()

    def get_first_paragraph(wikipedia_url):

        def find_p_with_b_start(tag):
            return tag.name == 'p' and tag.b
        
        response = requests.get(wikipedia_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        first_paragraph = soup.find(find_p_with_b_start)
        return first_paragraph
    
    def to_json_file(self, filepath):
        with open(filepath, 'w') as file:
            json.dump(self.leaders_data, file, indent=4)
    
