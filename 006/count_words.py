import os
import re
os.chdir(r'D:/python测试/')

def walk_dir(path):
    file_path = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.lower().endswith('txt'):#endswith() 方法用于判断字符串是否以指定后缀结尾
                file_path.append(os.path.join(root,f))
               # file_path.append(join(root, f))
    return file_path

def find_key_word(filepath):
    word_dic = {}
    filename = os.path.basename(filepath)#返回filepath最后的文件名
    with open(filepath,encoding='utf-8') as f:
        text = f.read()
        words_list = re.findall(r'[A-Za-z]+', text.lower())
        for w in words_list:
            if w in word_dic:
                word_dic[w] += 1
            else:
                word_dic[w] = 1
        sorted_word_list = sorted(word_dic.items(), key=lambda d: d[1])
        '''
        word_dic.items() 为待排序的对象；
        key=lambda x: x[1] 为对前面的对象中的第二维数据（即value）的值进行排序
        '''
        print (u"在%s文件中，%s为关键词，共出现了%s次" %(filename, sorted_word_list[-1][0], sorted_word_list[-1][1]))
if __name__ == "__main__":
    for file_path in walk_dir(os.getcwd()):
        find_key_word(file_path)
