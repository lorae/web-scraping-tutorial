from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

#########################################################################
## Section 1: Use Selenium to download the HTML file with dynamic content
#########################################################################
# Toggle headless mode
headless = False

# Set up Chrome options
chrome_options = Options()
if headless:
    chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)
#chrome_options.add_argument("--disable-gpu")  # Disable GPU usage
#chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
#chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Set up Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
url = "https://lorae.github.io/web-scraping-tutorial/"
driver.get(url)

# Get the HTML content of the page
html_content = driver.page_source

# Wait for 5 seconds as a special effect :)
time.sleep(5)

# Close the browser
driver.quit()

#########################################################################
## Section 2: Extract data from the HTML
#########################################################################
# use BeautifulSoup to parse the html_content
soup = BeautifulSoup(html_content, 'html.parser')
#print(soup)

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