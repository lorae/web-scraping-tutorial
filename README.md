# Purpose
The purpose of this repository is to act as a web scraping training ground for those hoping to develop their skills in Python. It was presented by Lorae Stojanovic to the Brookings Institution as part of the Brookings Data Network presentation series on June 20, 2024.

The repository has three main elements: 
1. **[Instructional slides](https://lorae.github.io/web-scraping-tutorial/advanced-web-scraping.slides.html)** 
These slides (produced using Jupyter) walk users through web scraping techniques such as:
   - Making network requests
   - Parsing HTML code
   - Using Selenium
   - Discovering hidden APIs
   - Rendering JSON data sets
2. **[Instructional webpage](https://lorae.github.io/web-scraping-tutorial/)** 
This webpage, hosted on GitHub, acts as an illustrative example website that users can web scrape directly as they follow along with instructions from the slides.

3. **[Sample code](https://lorae.github.io/web-scraping-tutorial/sample_code/)**
The code walks users through:
   - Web scraping static content using HTTP requests and parsing the response using the `beautifulsoup4` library
   - Web scraping dynamic content using the `selenium` library
   - Requesting APIs using the `requests` library

# Getting Started
If you'd simply like to view the educational materials, please navigate to:

**Instructional slides:** https://lorae.github.io/web-scraping-tutorial/advanced-web-scraping.slides.html

**Instructional website:** https://lorae.github.io/web-scraping-tutorial

**Instructional code:** https://lorae.github.io/sample_code

# Instructions for running the project

If you'd like to run the source code on your computer, proceed with the steps below.

## If you're running the project for the first time

1. **Navigate to the directory where you'd like to save the project**:
    ```sh
    cd your/path/to/your/desired/folder
    ```

2. **Clone the repository**:
    ```sh
    git clone https://github.com/lorae/web-scraping-tutorial
    ```

3. **Set your working directory in the repository**:
    ```sh
    cd web-scraping-tutorial
    ```

4. **Install Poetry**:

   Poetry is a dependency management and packaging tool for Python. Follow the instructions for your operating system to install Poetry. If you already have Poetry installed, you may safely skip this step.

    - **For bash/zsh (Linux/macOS):**
      ```sh
      curl -sSL https://install.python-poetry.org | python3 -
      ```

    - **For Windows PowerShell:**
      ```powershell
      (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
      ```

    After installation, ensure that Poetry is added to your PATH. You can verify the installation by running:
   ```sh
   poetry --version
   ```

6. **Install Dependencies**:
    Use Poetry to install the project dependencies and set up the virtual environment.
    ```sh
    poetry install
    ```

7. **Activate the Poetry virtual environment**:
    ```sh
    poetry shell
    ```



You are now set up and ready to work on the project!

## If you're running the project for any subsequent time

1. **Set your working directory in the repository**:
    ```sh
    cd your/path/to/web-scraping-tutorial
    ```
2. **Activate the Poetry virtual environment**:
    ```sh
    poetry shell
    ```
## To generate the .html slides using Jupyter:

TODO: explain how to run the .ipynb file 

## To run the website locally:

TODO

# Project Structure
The schematic below illustrates the basic file structure of the project. 

```
web-scraping-tutorial/
│
├── .gitignore
├── README.md # The file you are currently reading
├── advanced-web-scraping.slides.html # Formatted presentation slides
├── index.html # Produces instructional website
│
├── sample_code/
│ ├── requests_bs4_sc3raping.py # Sample code for scraping static content
│ ├── selenium_scraping.py # Sample code for scraping dynamic content
│ └── api_requests.py # Sample code for requesting APIs
│
├── slides_content/
│ ├── advanced-web-scraping.ipynb # Jupyter notebook producing presentation slides
│ └── images/ # contains images used in the slides
│   ├── all-http-requests-screenshot.png
│   ├── brookings-edu-screenshot.png
│   ├── client-server-request-response.png
│   ├── client-server.png
│   └── ...
│
└── web_content/ # Content used in index.html (instructional website)
  └── css/ # Styling for instructional website
  │ └── styles.css
  │ 
  └── data/ # Data used in index.html (instructional website) external requests
  │ ├── gdp-data.csv # Used to populate the GDP graph on index.html
  │ └── web-scraping-resources.json # Used to populate cards for external resources on index.html
  │
  └── images/ # Images used in index.html (instructional website) external requests
    ├── book.jpg
    ├── building_blocks.jpg
    ├── chat_box.jpg
    ├── computer_cloud.jpg
    └── ...
```


