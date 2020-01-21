from bs4 import BeautifulSoup
import requests
from htmlparser import *
import json

laureate_info_url = 'http://mattleinhauser.com/NobelPeaceLaureates/nobel_peace_laureates_list.html'
lecture_url = 'https://www.nobelprize.org/prizes/peace/1964/king/26142-martin-luther-king-jr-acceptance-speech-1964/'
lecture_url_response = requests.get(lecture_url, timeout=5)
info_url_response = requests.get(laureate_info_url, timeout=5)
soup = BeautifulSoup(info_url_response.content, "html.parser")
# soup = BeautifulSoup(lecture_url_response.content, "html.parser")
# raw_text_list = []
peace_laureates = []


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


for element in soup.findAll('table'):
    peace_laureate_object = \
        {
            "year": strip_tags(str(element.findAll('td', attrs={'class': 'Year'}))),
            "laureate_name": strip_tags(str(element.findAll('td', attrs={'class': 'Name'}))),
            "birth_country": strip_tags(str(element.findAll('td', attrs={'class': 'Birth Country'}))),
            "winning_reason": strip_tags(str(element.findAll('td', attrs={'class': 'Reason Given'})))
        }
    peace_laureates.append(peace_laureate_object)

# For MLK Jr.'s Nobel Lecture

# for text_element in soup.findAll('article', attrs={'class': 'page-content border-top entry-content'}):
#
# # Due to the way the web page is set up, we need to format the Nobel lecture first before saving it to the JSON
# raw_text_list = text_element.find('p', attrs={'class': 'smalltext'}).find_next_siblings('p', class_=False, id=False)
#
#     # Remove the last paragraph because it is a footnote
#     del raw_text_list[len(raw_text_list) - 1]
#
# # Create an array of "temporary" Beautiful Soup instances so we can get the text from each list element
# temp_soup = []

# for o in range(len(raw_text_list)):
#     temp_soup.append(BeautifulSoup(str(raw_text_list[o]), "html.parser"))
#     raw_text_list[o] = temp_soup[o].get_text()

with open('nobel_lectures.json', 'w') as outfile:
    json.dump(peace_laureates, outfile)
