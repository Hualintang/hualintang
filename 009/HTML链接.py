import os, re
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (variables, value) in attrs:
                if variables == 'href':
                    if re.match(r'http(.*?)', value):
                        print(value)

if __name__ == '__main__':
    with open('ceshi2.html',encoding='utf-8') as html:
        parser = MyHTMLParser()
        parser.feed(html.read())
