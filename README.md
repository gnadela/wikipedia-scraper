# Wikipedia Scraper 

The Wikipedia Scraper is a Python project that allows you to scrape data from Wikipedia pages of country leaders and store relevant information in a JSON file.


## Features

- Created in a self-contained development environment
- Queries an API to obtain a list of countries and their past political leaders
- Extracts and sanitize their short bio from Wikipedia
- Store the scraped data in a JSON file.


## Installation

Clone the repository:

```bash
    git clone https://github.com/gnadela/wikipedia-scraper
```


## Repo Structure
```
.
├── wikipedia_scraper_env
├── src/
│   ├── scraper.py
│   ├── utils.py
├── .gitignore
├── main.py
├── leader_briefs.json
└── README.md
```


## Usage

Run the main script:

```bash
    python main.py
```


The script includes WikipediaScraper scraper object that allows to structurally retrieve data from the API. The object contains these attributes:

- base_url: str containing the base url of the API (https://country-leaders.onrender.com)
- country_endpoint: str → /countries endpoint to get the list of supported countries
- leaders_endpoint: str → /leaders endpoint to get the list of leaders for a specific country
- cookies_endpoint: str → /cookie endpoint to get a valid cookie to query the API
- leaders_data: dict is a dictionary where you store the data you retrieve before saving it into the JSON file
- cookie: object is the cookie object used for the API calls

The object contains these methods:

- refresh_cookie() -> object returns a new cookie if the cookie has expired
- get_countries() -> list returns a list of the supported countries from the API
- get_leaders(country: str) -> None populates the leader_data object with the leaders of a country retrieved from the API
- get_first_paragraph(wikipedia_url: str) -> str returns the first paragraph (defined by the HTML tag <p>) with details about the leader
- to_json_file(filepath: str) -> None stores the data structure into a JSON file


## Timeline

This project took 3 days for completion.


## Personal Situation

This project was done as part of the AI Bootcamp at BeCode.org. This is my first web scraping project after starting to learn python programming 2 weeks prior.

Connect with me on [LinkedIn](https://www.linkedin.com/in/geraldine-nadela-60827a11/).