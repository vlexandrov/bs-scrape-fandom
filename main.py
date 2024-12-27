from bs4 import BeautifulSoup

# Load html from file path
file_path = "input/fandom-tama-wiki.html"
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# parse html
soup = BeautifulSoup(html_content, 'html.parser')

# find tables
tables = soup.find_all('table')

# create multiline output
output_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Filtered Tables</title>
</head>
<body>
"""

