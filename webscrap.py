from bs4 import Beautifulsoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    print(content)