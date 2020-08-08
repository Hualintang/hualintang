set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等

.isdigit()#检测字符串是否只由数字组成

.center()#居中

"{:^12s}".format('*')#format格式化

rq=list(map(int,m))#map转换格式

bin()：其他进制转二进制

oct()：其他进制转八进制

int()：其他进制转十进制

hex()：其他进制转十六进制

二进制、八进制、十六进制的形式

二进制：以“0b”开头，如：0b111为十进制的7

八进制：以“0”开头，如：026为十进制的22

十六进制：以“0x”开头，如：0x1f为十进制的31

reduce() 函数会对参数序列中元素进行累积

operator模块输出一系列对应Python内部操作符的函数https://blog.csdn.net/zhtysw/article/details/80510113

collections.Counter('hello world')#collections函数统计字符出现的次数

collections.namedturple()#创建一个和元组类似但更为强大的类型——具名元组（namedtuple），也就是构造一个带字段名的元组。

choice(deck)#choice() 方法返回一个列表，元组或字符串的随机项。

filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表

bisect模块bisect.bisect(seq, item, lo = 0, hi =len(list_name))在有序列表 seq 中查找 item 的位置，并且返回其 索引 (index)，使得插入item后序列依然保持有序https://blog.csdn.net/u014120401/article/details/78808476

collections.deque类是一个线程安全，可以快速从两端添加或删除元素的数据类型

heapq.nlargest(3, nums))#查找集合最大的三个元素
heapq.nsmallest(3, portfolio, key=lambda s: s['price'])上面代码在对每个元素进行对比的时候，会以 price 的值进行比较

heapq模块实现了一个适用于python列表的最小堆排序算法https://www.cnblogs.com/Joyce-song94/p/7149440.html

readlines把文件的全部内容读到内存，并解析成一个list，当文件体积很大时，需要占用很多内存

0,[],(),{},'',False,None布尔值为False

dict={'a':24,'g':52,'i':33,'k':12}#sorted(dict.items(),key=lambda x:x[1])

copy()只拷贝数据集合第一层，deepcopy()拷贝所有层

capwords()#将字符串中所有单词首字母大写

maketrans()函数创建转换表，结合translate()比replace()高效
