import json
from src.scraper import WikipediaScraper
from src.utils import read_json, write_json

scraper = WikipediaScraper()
countries = scraper.get_countries() # Loop through each country and query the /leaders endpoint
print(countries)
for country in countries: 
    scraper.get_leaders(country) 

leaders_per_country = scraper.leaders_data
        
wikipedia_urls = []
for country, leaders in leaders_per_country.items():
    # Iterate over each leader and get their wikipedia_url
    for leader in leaders:
        url = leader['wikipedia_url']
        wikipedia_urls.append(url)

leader_paragraphs = []
for url in wikipedia_urls:
    first_paragraph = WikipediaScraper.get_first_paragraph(url)
    cleaned_paragraph = first_paragraph.text
    print(url)
    print(cleaned_paragraph)
    leader_paragraphs.append(cleaned_paragraph)

write_json(leader_paragraphs, 'leader_briefs.json')
