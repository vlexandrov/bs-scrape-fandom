from bs4 import BeautifulSoup

# Load html from file path
file_path = "input/fandom-tama-wiki.html"
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()