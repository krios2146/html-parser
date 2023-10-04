import re

import requests
from bs4 import BeautifulSoup


def main():
    print("Getting html from site...")
    html = get_html_from_url("https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx")

    print("Parsing words...")
    words = parse_words(html)

    print(f"Creating .txt file with {len(words)} words...")
    create_file(words)


def get_html_from_url(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("GET is not OK")
        exit()

    return response.text


def parse_words(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all(href=re.compile("/how-to-use/*"), target="_blank")

    words = []
    for link in links:
        word = link.text
        words.append(word)

    return words


def create_file(words):
    file_path = "dictionary.txt"

    with open(file_path, "w") as file:
        for word in words:
            file.write(word + "\n")


if __name__ == '__main__':
    main()
