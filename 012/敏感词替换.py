import os
os.chdir('D:python测试/')
def trans_to_words():
    type_in = input(">")
    with open('miganci.txt',encoding='utf-8') as f:
        text = f.read()
    for i in text.split("\n"):
        if i in type_in:
            type_in = type_in.replace(i, '**')
    print(type_in)
trans_to_words()
