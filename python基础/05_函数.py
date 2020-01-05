#定义一个函数
def test():
    print("hello")
#执行函数
test()

#函数对象
#把test函数对象复制给var 这时候var就是test的对象
var=test
#执行var函数
var()

#命名规范
#驼峰命名法
def getApplepie():  #单词首字母大写
    print("this is apple")
#下划线命名法
def get_apple_pie():
    print("this is apple")
#函数参数
def funcA(a):   #a叫做形参
    print(a)
#执行函数10叫做实参
funcA(10)

#实参给形参的传参顺序是从左到右
def funcB(a,b,c):
    print(a,b,c)
#执行参数
funcB(1,2,3)

#指定参数
def funcC(a,b,c):
    print(a,b,c)
funcC(1,b=3,c=2)

#默认传参1
def funcD(a,b,c=1):     #若形参中有关键字传参和非关键字传参 关键字传参需要放在最后面
    print(a,b,c)
funcD(a=1,b=2)

#关键字实参
def funcE(a,b,c=4):
    print(a,b,c)
funcE(1,b=2,c=3)    #若实参中有关键字传参和非关键字传参 关键字传参需放在最后面

#实参传了默认参数的值的时候，优先取实参的参数，实参未传时再取默认的参数
def funcF(a,b,c=4):
    print(a,b,c)
funcF(a=1,b=2,c=3)

############################################

def testA():
    print("hello")
def testB(a):   #def 函数名 函数名后面的（）内的参数a可以是任何东西
    a()         #testB函数a()内接收了形参a 而形参a最后接收了testA的对象
testB(testA)    #此处（）内填写的是testA函数对象 所以执行testB函数时 执行的内容为hello

############################################
def hanshu(var):
    print(var)
hanshu(10)      #定义函数 def hanshu(var)   已经传入了形参 执行函数hanshu 需要传入实参才会执行

def hanshuA(var):
    print(var)
def hanshuB(a,b):
    a(b)
hanshuB(hanshuA,1)  #hanshuB()中内容分开传入最后在代码块中合并

#多类型传参
# 非关键字包裹传参（元组多类型传参）（多输出的内容会变为元组）
# def funcI(a,b,*args):
#     print(a,b,args)
# funcI(1,2,3,4,5,6,"",11)

#关键字包裹传参 字典多类型传参 （多输出的内容会变成字典）
def funcj(a,b,**kwargs):
    print(a,kwargs)
funcj(1,b=10,c='str',d=1)

#非关键字包裹传参  关键字包裹传参字典元组类型多传参（包裹传参）
def funcK(a,b,*args,**kwargs):
    print(a,b,args,kwargs)
funcK(1,2,3,4,5,d=1,e=2)

# 解包裹
# *
tupelvar=(10,20)
listvar=[10,20]
strvar='ad'
setvar={10,20}

def funcL(a,b):
    print(a,b)
funcL(*tupelvar)
funcL(*listvar)
funcL(*strvar)
funcL(*setvar)

#**的传参方式
#传参的key需要于形参名称相对应
dictvar={
    'name':'jsaon',
    'job':'it'
}
def funcW(name,job):
    print(name,job)
funcW(**dictvar)

#函数默认不加return关键字，默认return None
def funcA():
    print("hello1")
var=funcA()
print(var)
#函数A可以返回多个值
#使用一个变量去接收多个返回值的时候返回一个元组
def A():

    return  1,2,3
A()         #不使用打印时只会输出里面的方法
var=A()
print(var)  #需要打印才会输出返回值

#使用多个变量去接返回的数据（需要一一对应）
var,var1,var2=A()
print(var,var1,var2)

#if else 判断return多个结果（方式一）
def B(a):
    if a==10:
        return  True
    else:
        return False
result=B(1)
print(result)
print(B(2))

#if else 判断return多个结果（方式二）
def C(a):
    if a == 10:
        flag=True
    else:
        flag=False
    return flag
result=C(10)
print(result)

#return 作用  1.获得函数的返回值 2.具备break的功效
def D():
    for i in range(1,10):
        if i  == 5:
            return  i
result=D()
print(result)

#函数变量概念
value=10    #全局变量（所有地方都可以调用到的变量）
def E():
    value1=20   #(局部变量)函数内定义的变量
    return value1
result=E()
print(result)

#global 声明全局变量关键字
def F():
    global value    #声明全局变量并修改
    value+=90
    print(value)
    return value
F()
# result=F()
# print(result)

# nonlocal  #修改嵌套作用域中的变量则需要 nonlocal关键字
def nonlocal_test():
    count = 0
    def test2():
        nonlocal count  #nolocal关键字声明
        count += 1
        return count
    return test2
val = nonlocal_test()
print(val())

# #nonlocal   修改嵌套作用域中的变量则需要 nonlocal 关键字
# def outer():
#     num=10
#     def inner():
#         nonlocal num    #nolocal关键字声明
#         num+=10
#         print(num)
#     return inner
# val=outer()
# print(val())

listvar=[10,20]
def Q():
    global listvar  #改变变量listvar的类型
    listvar=10
Q()
print(listvar)

dictvar={'name':"jason"}
def J():
    global dictvar  #改变变量dictvar的类型
    dictvar = 11
J()
print(dictvar)

##练习题
#函数来编辑一个计算器（加减乘除）（return关键字返回结果）
def calculator(num1,num2,num3):
    if num3=="+":
        print(num1+num2)
    elif num3=="-":
        print(num1-num2)
    elif num3=="*":
        print(num1*num2)
    elif num3=="/":
        print(num1/num2)
print(calculator(5,5,"*"))


# 练习题 用函数方式
strvar = 'fasjdfjka21jsn3jsdsd7kdn9k8nc'
# 分别输出英文和数字
# 分别输出英文的总数和数字的总数
# 我希望最后输出的结果是
# 英文字符有一共有N个
# 数字字符有一共有N个
# 方法一的提醒
# 判断是否是数字
var = 'admin'
result = '1'.isdigit()
print('结果是',result)

# # 判断是否是英文
# result2 = 'a'.isalpha()
# print('结果是',result2)

def test():
    Englishstr=[]   #定义一个空的列表
    numstr=[]       #定义一个空的列表
    for i in strvar:
        if i.isdigit():
            numstr.append(i)
        elif i.isalpha():
            Englishstr.append(i)
    print(Englishstr)
    print(numstr)
    i=len(Englishstr)
    j=len(numstr)
    print(i)
    print(j)
    print(i+j)
test()









