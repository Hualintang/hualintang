import os
import json
import xlwt
os.chdir('D:/python测试/')
def read_txt(path):
    with open(path, 'r',encoding='utf-8') as f:
        text = f.read()
        text_json = json.loads(text)
    return text_json
  def save_into_excel(content_dict, excel_name):
    wb = xlwt.Workbook()#设置一个编码
    ws = wb.add_sheet("student",  cell_overwrite_ok=True)#确认同一个cell单元是否可以重设值
    row = 0
    col = 0

    for k, v in sorted(content_dict.items(),key=lambda d:d[0]):#以列表返回可遍历的(键, 值) 元组数组
        ws.write(row, col, k)
        for i in v:
            col += 1
            ws.write(row, col, i)

        row += 1
        col = 0

    wb.save(excel_name)
read_content = read_txt(os.path.join(os.path.split("")[0], 'student.txt'))
save_into_excel(read_content, 'student.xls')
