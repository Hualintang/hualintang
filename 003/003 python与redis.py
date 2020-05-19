#将生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中
import uuid
import redis

def create_code(num, length):
    result = []
    while True:
        uuid_id = uuid.uuid1()
        temp = str(uuid_id)[:length]
        temp1=temp[4:23]
        #if not temp in result:#可省略
            result.append(temp1)
        if len(result) == num:
            break
    return result
  
def save_to_redis(num_list):
    r = redis.Redis(host='localhost', port=6379, db=0)
    for code in num_list:
        r.lpush('code',code)#将值添加到列表头部

save_to_redis(create_code(200,20))
