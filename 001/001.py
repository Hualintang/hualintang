#做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import uuid

'''
print(uuid.uuid1())
print(uuid.uuid4())
'''

def create_code(num, length):
    result = []
    while True:
        uuid_id = uuid.uuid1()
        temp = str(uuid_id)[:length]
        temp1=temp[4:23]
        if not temp in result:
            result.append(temp1)
        if len(result) == num:
            break
    return result
  print(create_code(200, 23))
