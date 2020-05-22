import os
from bs4 import BeautifulSoup
os.chdir('D:/python测试/')

import requests
from bs4 import BeautifulSoup
import re
import pdb

'''
url = 'http://www.zhuixinfan.com/main.php'
html = requests.get(url)
soup = BeautifulSoup(html.text,"html.parser")
print(soup.body.text.encode('GBK','ignore').decode('GBK'))
'''
'''
def find_the_content(path):
    with open(path) as f:
        text = BeautifulSoup(f, 'lxml')
        content = text.get_text().strip('\n')
        return content.encode('gbk','ignore')
if __name__ == '__main__':
    print(find_the_content('ceshi.html'))
'''   
