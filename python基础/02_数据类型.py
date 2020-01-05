# 数据类型
#Number(数字) str（字符串） list(列表) tuple（元组） dict(字典) set（集合） bool（布尔）
#不可变数据类型（值类型） Number tuple str
#可变的数据类型（引用类型）list dict set

#可变与不可变的定义
#可变：当有需要改变对象本身内部的值的时候，这个对象的id不发生变化
#不可变：当有需要改变对象本身内部的值的时候，这个对象的id发生变化
#对不可变类型的变量需要重新来赋值，实际上是重新传教一个不可变类型的对象，并将原有的变量指向新的对象
#可使用函数id来查看变量id

#数字类型
#int（整数） float（浮点数）

#列表
listvar= [1,2,3,4,5]    #定义一个列表
#列表的增删改查

#增
#append 默认在末尾添加元素
listvar.append(6)
print(listvar)
#insert 指定位置添加元素（通过下标添加元素）
listvar.insert(6,7)
print(listvar)

#删
#pop 删除末尾元素（默认删除末尾元素）
listvar.pop()
print(listvar)
#pop 通过元素的下标删除指定位置的元素
listvar.pop(0)
print(listvar)
#通过remove 通过元素的值删除元素(存在多个相同的值的时候会删除第一个)
listvar.remove(2)
print(listvar)
#del 通过索引范围删除元素
del listvar[0:1]
print(listvar)

#remove(x) 删除列表中第一个为x的值
lst=[1,2,3,4,5] #定义一个列表
print(lst.remove(2))  #这种写法的输出的remove函数的返回值，但该函数没有返回值默认返回None
lst.remove(1)

#查
#通过index(x) 查询列表中元素的下标 返回列表中与x值相等的第一个值得索引
lst=[1,2,3,4,5]
print(lst.index(1))
#修改
lst=[1,2,3,4,5]
#通过lst的下标来重新赋值 起到修改元素的作用
lst[1] = 22
print(lst)

#列表（可变）（引用类型）
#将列表中的数据数字类型转换为字符串
lst=[1,2,3,4,5] #定义一个列表
lst1=[str(i) for i in lst]  #定义一个列表lst1，再使用for循环迭代lst
                                 # 每次迭代的值再赋予i 形成一个新的列表 再通过str（）进行类型转换 最后所有的值返回一个新的列表
print(lst1)

lst2=[]                 #定义一个空的列表
for i in lst:           #通过for循环遍历lst
    lst2.append(str(i)) #str（i）将遍历的值i转为字符串再通过append函数添加进lst2类别
    print(lst2)         #最后打印lst2 里面的数据类型为字符串

lst3="".join(lst1)  #join 将序列中的元素链接生成一个新的字符串
print(lst3)
print(type(lst3))

#统计某个元素在列表中出现的次数count统计元素1出现的x次
lst=[1,2,3,4,5]
lst1=lst.count(1)
print(lst1)
#reverse 将列表中的元素反转
lst=[1,2,3,4,5]
lst.reverse()
print(lst)
#len 获取对象长度
lst=[1,2,3,4,5]
print(len(lst))

#通过索引查询序列中的元素（序列为：字符串、列表、元组、字典）（元素类型为数字、字符串）
#python中有两种索引方式，从左往右以0开始，从右往左以-1开始
#截取语法格式如下，变量[头下标：尾下标：步长]
lst=[1,2,3,4,5]
print(lst[0:3])     #头上标为0，尾下标为3，步长默认为1，尾下标默认不取
                    #输出第一个到第四个元素
print(lst[0])       #输出第一个元素
print(lst[4::-1])   #输出从第五个元素到最后一个元素 步长为-1从右往左取
print(lst[::-1])    #输出从右往左的所有元素
print(lst[2::])     #输出从第三个元素到后面的所有元素

#列表转换为其他类型
lst=[1,2,3,4,5]
print(tuple(lst))   #转换为元组
print(str(lst))     #列表里面的数据类型不能直接转换为字符串！！！
print(set(lst))     #转换为集合

#列表去重 多种方法
#1.可将列表先转换为集合再转换为列表 去重后顺序会发生变化
lst=[1,5,1,2,3,4,5,6]   #定义一个列表
setvar=set(lst)         #将列表先转换为集合
lstvar=list(setvar)     #将集合再转换为列表
print(lstvar)           #打印去重后的列表

#如果不想排序发生变化 可以使用sort函数  示例：list.sort( key=None, reverse=False)
#key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
#reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
lst=[1,5,1,2,3,4,5,6]       #定义一个列表
setvar=set(lst)             #将列表先转换为集合
lstvar=list(setvar)         #将集合再转换为列表
lstvar.sort(key=lst.index)  #通过sort函数 key对应lst的下标进行排序
print(lstvar)               #打印去重后的列表

#2. fromkeys 将列表转换为字典且字典的键是唯一的 起到了去重的作用
#列表转换为字典 字典再取出key值，返回的是一个元组最后通过list再转换为列表
lst=[1,5,1,2,3,4,5,6]           #定义一个列表
# dictvar=dict.fromkeys(lst)    #通过dict.fromkeys将列表转换为字典
# listvar=list(dictvar.keys())  #再取出字典的key值返回了元组 最后再转换为列表
# print(listvar)
listvar=list(dict.fromkeys(lst).keys())
print(listvar)

#3.使用for循环遍历 使用for循环方法数据的顺序不会发生变化
lst=[1,5,1,2,3,4,5,6]
listvar=[]
for i  in lst:
    if i not in listvar:
        listvar.append(i)
print(listvar)

#字符串不可变 需改变字符串时需要重新赋值给一个变量来接收
#字符串 值类型 不可变 有序的
#字符串（字符串对象处理方法）
#in 方法判断内容是否存在字符串中
strvar="123@456.com"    #定义一个字符串
print('23'in strvar)    #判断"23"是否存在strvar中 如果存在则返回Ture
print("789" in strvar)  #判断"789"是否存在strvar中 如果不存在则返回false
# not 方法返回表达式结果式相反值，如果结果为真则返回假
strvar="123@456.com"
print("23" not in strvar)   #判断"23" 不存在strvar里面 执行结果为False
print("789"not in strvar)   #判断"789"不存在strvar里面 执行结果为True

#is 判断内存地址是否相同 内存地址python中所有数字、字符串、list等值，创建是会分配内存空间
#变量通过引用的方式使用它们。比如a=1和b=1，id(a)和id(b)的输出一样，表示a和b都是指向相同的内存地址
#即引用了同一个不可变对象；但是a=[1]和b=[1],id（a）和id（b）将输出不一样的值，a和b是指向不同的内存地址
#即引用了不同的可变对象，说明各可变对象是相互独立的，内存中有独立的内存地址
a="1234"
b='1234'
print(a is b)

#split 分隔 将字符串 进行分隔返回的结果类型为列表
#123@456.com 转换为456@123.com
i="1234@456.com"    #定义一个字符串
i_list=i.split(".") #按照.号来分隔 字符串，返回的结果类型为列表
print(i_list)
i_list1=i_list[0].split("@")    #再通过@来分割
print(i_list1)
print("{}@{}.{}".format(i_list1[1],i_list1[0],i_list[1]))

#replace() 方法把字符串中的old（旧字符串）替换成new（新字符串）
#123@456.com 转换为456@123.com
i="123@456.com"
j="456@123.com"
print(i.replace(i,j))
print(i.replace("123@456.com","456@123.com"))
#将123@456.com转换为123@456.net
i="123@456.com"
print(i.replace(".com",".net"))

#form格式化字符串
strvar='admin'
intvar=10
floatvat=1.31
listvar=[10,20]
print("测试报告{}".format(listvar))
print("测试报告{}///////////{}{}{}".format(strvar,intvar,floatvat,listvar))

#元组（不可变）值类型 不可变类型
#元组不可增删改
#元组也可以通过下标查询序列中的值
tuplevart=("admin",1,2,3,4,5,(1,2,3,4,5))
#元组里面有单个数值的时候需要添加，如果不添加逗号 输出的类型是数据类型
tuplevart=(10)
tuplevart1=(10,)
print(type(tuplevart))
print(type(tuplevart1))

#字典
#字典（dict）属于键值对类型 key:value
#key的值是唯一
#字典展示的顺序是无序的
dictvar={"name":"jsaon","key":"111"}
#查询
print(dictvar["name"])

#get方法含有默认值
#key 字典中要查找的键
#default 如果指定的键不存在时，返回默认值
#不指定默认值
print(dictvar.get("name1"))     #指定的key不存在时返回默认值None
print(dictvar.get("name1","设置返回值")) #指定的key不存在时可以设置默认返回值
print(dictvar.get("key"))
#改 通过key重新来赋值 起到修改value
print("原本的字典值是",dictvar)
dictvar["name"]="tim"
print("现在的字典值是",dictvar)
#增加 通过新建key：value来赋值
print("原本的字典的键值是",dictvar)
dictvar["age"]=18
print("现在的字典的键值是",dictvar)
#删除 通过pop（key）
dictvar.pop("age")
print(dictvar)

#取出hello
dictvar1 = [(10, 20, 30, {'name': [10, 20, 30, {'admin': 'hello'}]})]
print(dictvar1[0][3]["name"][3]["admin"])

#集合（去重功能）
#集合（set）是一个无序的不能重复的元素序列
#可以使用大括号{}或者set()函数创建集合，注意：创建一个空集合必须用set（）而不是{}
#因为{}可以创建一个空字典
setvar={12,3,4,5}   #定义个集合
print(setvar)
print(type(setvar))
#定义一个空集合
setvar1=set()
print(setvar1)
print(type(setvar1))
#增 add
setvar.add(1)
print(setvar)
#删 pop
setvar.pop()
print(setvar)

#面试经典题 列表去重
listvar=[10,10,20,20,30]
print('原本的列表是',listvar)
listvar2=set(listvar)
print('转换后的是',listvar2)
listvar3=list(listvar2)
print(listvar3)

#值类型
#在python中，数值（int整型，float浮点型），布尔型，字符串，元组属于值类型，本身不允许被修改（不可变类型）
#数值的修改实际上是让变量指向了一个新的对象（新创建的对象）
#所以不会发生共享内存问题。
#引用类型
#在python中，列表，集合，字典是引用类型，本身允许修改（可变类型）

#布尔值类型
boolvar=True
print(boolvar)
#表示0，None，空的量(None)代表假（False）
#1代表真（True）非空的量（字符串等类型），非零的数值（数值类型）

