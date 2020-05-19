#任一个英文的纯文本文件，统计其中的单词出现的个数
import re

def count_the_words(path):
    with open(path) as f:
        text = f.read()
        words_list = re.findall(r'[a-zA-Z0-9]+', text)#'[a-zA-Z0-9]+'等同于'\w+'
        count = len(words_list)
    return count

nums = count_the_words('danci.txt')
print(nums)
