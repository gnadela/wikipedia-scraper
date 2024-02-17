from src.scraper import WikipediaScraper
from src.utils import write_json

scraper = WikipediaScraper()
countries = scraper.get_countries() # Get the list of countries

# Retrieve leaders data for each country
for country in countries: 
    scraper.get_leaders(country) 

# Get Wikipedia URLs of leaders        
wikipedia_urls = []
for leaders in scraper.leaders_data.values():
    for leader in leaders:
        url = leader.get('wikipedia_url')
        if url:
            wikipedia_urls.append(url)

leader_paragraphs = []
for url in wikipedia_urls:
    # Retrieve the first paragraph for each leader's Wikipedia page
    first_paragraph = WikipediaScraper.get_first_paragraph(url)
    if first_paragraph:
        cleaned_paragraph = first_paragraph.text.strip() # remove trailing or leading white spaces
        print(url)
        print(cleaned_paragraph)
        leader_paragraphs.append({'url': url, 'first_paragraph': cleaned_paragraph})
    else:
        print((f"Unable to retrieve first paragraph for {url}"))
        
write_json(leader_paragraphs, 'leader_briefs.json')
