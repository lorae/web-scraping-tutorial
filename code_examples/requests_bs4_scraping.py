import requests
from bs4 import BeautifulSoup

my_headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/122.0.6261.112 Safari/537.36'
    ),
    'Accept': (
        'text/html,application/xhtml+xml,application/xml;q=0.9,'
        'image/avif,image/webp,image/apng,*/*;q=0.8,'
        'application/signed-exchange;v=b3;q=0.7'
    )
}

my_url = "https://lorae.github.io/web-scraping-tutorial/"

session_arguments = requests.Request(method='GET', 
                                     url=my_url, 
                                     headers=my_headers)
session = requests.Session()
prepared_request = session.prepare_request(session_arguments)
response: requests.Response = session.send(prepared_request)

print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup)

# Select elements corresponding to table rows
elements = soup.select('tr.data-row')

# Initialize lists for data output
Titles = []
Authors = []

for el in elements:
    title = el.find('td', class_='title').text
    author = el.find('td', class_='author').text
    
    # Add data to lists
    Titles.append(title)
    Authors.append(author)

print(Titles)
print(Authors)

# NOTE: This code is intentionally nonfunctional. See slides for more
# information.

# Scrape titles and links
elements = soup.select('div.digest-card__title a')
# Initialize lists
Titles = []
Links = []
for el in elements:
    print(el)
    # Obtain the link to the resource
    link =  el['href'] # 'href' is a HTML lingo for hyperlinks.
    # Obtain the title of the resource
    title = el.text

    # Append the entries to each list
    Titles.append(title)
    Links.append(link)

# Print the results
print(Titles)
print(Links)