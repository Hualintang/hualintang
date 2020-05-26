import os
import urllib
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, urlparse
import requests
os.chdir('D:/迅雷下载/')

def download_pic(url):
    image_content = urllib.request.urlopen(url).read()
    file_name = os.path.basename(urlsplit(url)[2])
    output = open(file_name, 'wb')
    output.write(image_content)
    output.close()



def catch_tieba_pics(url):
    content = urllib.request.urlopen(url)
    bs = BeautifulSoup(content, 'lxml')
    for i in bs.find_all('img', {"class": "BDE_Image"}):#根据源码找标签
        download_pic(i['src'])




#if __name__ == '__main__':
catch_tieba_pics('https://tieba.baidu.com/p/2166231880?red_tag=2074967928')
