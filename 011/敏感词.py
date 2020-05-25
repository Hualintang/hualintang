import os
os.chdir('D:python测试/')

def trans_to_words():
    type_in = input(">")
    judge_flag = False
    with open('ceshi3.txt',encoding='utf-8') as f:
        text = f.read()

    for i in text.split("\n"):
        if i in type_in:
            judge_flag = True

    if judge_flag:
        print("Freedom")
    else:
        print("Human Rights")



if __name__ == "__main__":
    while True:
        trans_to_words()
