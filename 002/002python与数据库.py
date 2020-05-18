#将生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import uuid
import MySQLdb
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
    
def save_to_mysql(num_list):
    conn = pymysql.connect(host='localhost', user='root', passwd='root', port=3306)
    cur = conn.cursor()
    sql_create_database = 'create database if not exists activecode_db'
    cur.execute(sql_create_database)
    conn.select_db("activecode_db")
    sql_create_table = 'create table if not exists active_codes(active_code char(32))'
    cur.execute(sql_create_table)
    cur.executemany('insert into active_codes values(%s)', num_list)
    conn.commit()
    cur.close()
    conn.close()
    
code_num = create_code(200, 20)
save_to_mysql(code_num)
