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

# processing
for index, table in enumerate(tables):
    output_html += f"<h2>Table {index + 1}</h2>\n"
    """
    tbody = table.find('tbody')
    if tbody:
        # remove icons, stored in divs in some column
        rows_to_remove = tbody.find_all('tr', recursive=False)
        for row in rows_to_remove:
            # if row contains div with icons, remove
            if row.find('div', class_='center'):
                row.decompose()
    """
    output_html += str(table)
    output_html += "\n"

# close multiline for exporting
output_html += """
</body>
</html>
"""

output_file_path = 'output/output_tables.html'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(output_html)