# Purpose
The purpose of this repository is to act as a web scraping training ground for those hoping to develop their skills in Python. It was presented to the Brookings Institution as part of the Brookings Data Network presentation series on XXX XX, 2024.

The repository has two main elements: 
1. An [instructional slideshow](https://lorae.github.io/web-scraping-tutorial/advanced-web-scraping.slides.html) produced as a Jupyter notebook, which walk users through web scraping techniques and code
2. An [instructional webpage](https://lorae.github.io/web-scraping-tutorial/), hosted on GitHub, which users can practice their scraping skills on. The webpage exhibits several features that allow users to practice skills such as:
   - Making network requests
   - Parsing HTML code
   - Using Selenium
   - Discovering hidden APIs
   - Rendering JSON data sets

# Getting Started
If you'd simply like to view the educational materials, please navigate to:

**Instructional slides:** https://lorae.github.io/web-scraping-tutorial/advanced-web-scraping.slides.html

**Instructional website:** https://lorae.github.io/web-scraping-tutorial

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

4. **Install Poetry** (Skip this step if Poetry is already installed):
    Poetry is a dependency management and packaging tool for Python. Follow the instructions for your operating system to install Poetry. If you already have Poetry installed, you may safely skip this step.

    - For bash/zsh (Linux/macOS):
      ```sh
      curl -sSL https://install.python-poetry.org | python3 -
      ```

    - For Windows PowerShell:
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

7. **Activate the Virtual Environment**:
    Activate the virtual environment created by Poetry.

    ### For bash/zsh (Linux/macOS) and Windows PowerShell:
    
    ```sh
    poetry shell
    ```



You are now set up and ready to work on the project!

## If you're running the project for any subsequent time

TODO: explain how to run the .ipynb file to produce the Jupyter slides and how to run the website locally




