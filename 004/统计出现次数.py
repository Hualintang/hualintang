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

#获取文本文件字符数

import collections
import pprint
def main():
    file_input = input('File Name: ')
    try:
        with open(file_input, 'r',encoding='utf-8') as info:
            count = collections.Counter(info.read().upper())
    except FileNotFoundError:
        print("Please enter a valid file name.")
        main()

    value = pprint.pformat(count)
    print(value)

if __name__ == "__main__":
    main()
