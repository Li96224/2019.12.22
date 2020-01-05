intvar=10
#赋值运算符
#为intvar赋值+1
intvar=intvar+1
#等价上面
intvar+=1
print(intvar)

#字符串
strvar="admin"
strvar2="nihao"
# +号拼接了字符串
print(strvar+strvar2)

#列表
listvar=[10,20]
listvar2=[1,2]
print(listvar+listvar2)
#元组
tuplevar=(10,20)
tuplevar2=(100,200)
print(tuplevar+tuplevar2)

#了解强类型语音和弱类型语言的差别
strvar="admin"
intvar=1
#python属于是强类型语言 不同类型的值不能直接相加
# print(strvar+intvar)    #会报错

strvar="admin"
boolvar=True

#注意 ==和is区别
# == 判断具体的值是否相等
print(strvar==boolvar)

#字符串值转换成bool来判断
print(bool(strvar) is True)