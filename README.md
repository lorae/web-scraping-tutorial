# Purpose
The purpose of this repository is to act as a web scraping training ground for those hoping to develop their skills in Python. It was presented to the Brookings Institution as part of the Brookings Data Network presentation series on XXX XX, 2024.

### Instructional slides
This repository produces slides th, produced using a Jupyter notebook, which can be found here: [ADD LINK!]

### Instructional webpage
This repository also produces a [web scraping training ground](https://lorae.github.io/web-scraping-tutorial/), a website meant to demonstrate the basic principles of website organization and allow users to test their skills in areas such as:
- network requests
- HTML parsing
- Selenium
- "hidden" API scraping

Users can follow along with the web scrapign trianing slides (add link here) to get a step-by-step tutorial on the ways that the data on the instructional webpage can be scraped.

# Access the web scraping training ground here!
https://lorae.github.io/advanced-web-scraping/
# Access the web scraping training slides here!
[ADD LINK]

# Web Scraping Tutorial

# Getting Started
Follow these setup instructions if you'd like to clone the repository on your computer.

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

4. **Install Poetry** (Skip this step if Poetry is already installed):
    Poetry is a dependency management and packaging tool for Python. Follow the instructions for your operating system to install Poetry. If you already have Poetry installed, you may safely skip this step.

    ### For bash/zsh (Linux/macOS):

    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    ### For Windows PowerShell:

    ```powershell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    ```

    After installation, ensure that Poetry is added to your PATH. You can verify the installation by running:
    
    ```sh
    poetry --version
    ```

5. **Install Dependencies**:
    Use Poetry to install the project dependencies and set up the virtual environment.

    ```sh
    poetry install
    ```

6. **Activate the Virtual Environment**:
    Activate the virtual environment created by Poetry.

    ### For bash/zsh (Linux/macOS) and Windows PowerShell:
    
    ```sh
    poetry shell
    ```

You are now set up and ready to work on the project!




