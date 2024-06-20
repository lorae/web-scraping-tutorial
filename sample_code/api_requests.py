import requests

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

my_request_url = "https://lorae.github.io/web-scraping-tutorial/web_content/data/web-scraping-resources.json"

session_arguments = requests.Request(method='GET', 
                                     url=my_request_url, 
                                     headers=my_headers)
session = requests.Session()
prepared_request = session.prepare_request(session_arguments)
response: requests.Response = session.send(prepared_request)

json_data = response.json()
json_data

# Now json_data is a list of dictionaries, each representing an article/resource
for article in json_data:
    title = article['title']

    print(title)