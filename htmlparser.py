# This function comes from StackOverflow user Eloff at:
# https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python/925630#925630 And improved for Python
# 3.2+ by another StackOverflow user Thomas K. here:
# https://stackoverflow.com/questions/11061058/using-htmlparser-in-python-3-2


from abc import ABC
from html.parser import HTMLParser


class MLStripper(HTMLParser, ABC):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)