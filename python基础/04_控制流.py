#for循环
listvar=[1,2,3,4]

#生成一个从1到7的列表
result=range(1,8)
print(result)
#这里的range()函数返回的对象在python3中并不是list类型的，也不继承list类型
#python3中的range()等于python2中的xrang()
#它其实是一个生成器，每次取值后生成下一个值，目的是节约内存和运算资源
#如果想得到list，则需要强制转换
print(list(result))

#for 循环 迭代的对象 序列及字典
print("原本的列表是",listvar)
#初始变量
for i in range(1,6):    #range(1,6)上标为1,下标为6,步长默认为1
    print(i)
listvar2=[10,20,30]
#遍历列表
#i 最开始的初始变量
#遍历 把序列中有数值全部都输出一遍
#遍历的方式一
for i in listvar2:
    print(i)
#遍历的方式二
for i in range(len(listvar2)):  #通过range再通过len获取下标
    print(i)
#遍历方式三
for i in range(len(listvar2)):  #通过range再通过len获取下标
    print(listvar2[i])          #再通过下标输出对应的值

#遍历元组
tuplevar=(100,200,300)
for i in tuplevar:
    print(i)
#遍历字符串
strvar="admin"
for i in strvar:
    print(i)
#遍历字典（输出字典的key）
dictvar={
    'name':'jason',
    'job':'it'
}
#遍历字典 初始值i返回的值是key
for i in dictvar:
    print(i)
#处理字典遍历key的方式一（遍历时把key的值赋予i 再通过key 输出value）
for i in dictvar:
    print(dictvar[i])
#处理字典遍历key的方式二 #itmes Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组
for i in dictvar.items():
    print(i)
#处理字典遍历key的方式三 dict.key 通过key获取value
for i in dictvar.values():
    print(i)

#嵌套循环
#i 转一个大圈
#j 转九个大圈
#j 转一个圈
#z 转九个圈
# for i in range(1,10):
#     print('iiiiiiiiiiiiiiii is ',i )
#     for j in range(1,10):
#         print('jjjjjjjjjjjjj is ',j)
#         for z in range(1,10):
#             print('zzzzzzzzzzzz is ',z)

#打印一个九九乘法表
for i in range(1,10):       ##遍历范围 1,2,3,4,5,6,7,8,9
    for j in range(1,i+1):  #循环第一遍是i的值是1  j遍历的范围是1 再由此逐步添加计算
        print("{}*{}={}".format(i,j,i*j),end="")     #end = “ ”的意思就是在每个计算的结尾处加个空格
    print("")

i=1
while i<=9:
    j=1
    while j<=i:
        print("{}*{}={}".format(i,j,i*j),end="")
        j=j+1
    print("")
    i = i + 1

for i in range(1,10):
    j=1
    while j<=i:
        print("{}*{}={}".format(j,i,i*j),end="")
        j+=1
    print()

i=1
while i<=9:
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,i*j),end="")
    print("")
    i+=1

#while 循环
#while 语句后面加的是条件
var=3
while var>0:    #当条件为True时永远执行 当条件为false时循环不执行
    var=var-1
    print(var)

var1=0
while var1<5:
    var1+=1
    print(var1)

#whlie循环求1到100的和
sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print(sum)

#for循环求1到100的和
sum=0
for i in range(1,101):
    sum+=i
print(sum)

#if 后面的是我们的条件语句
#需要保证执行的代码块在if语句的下面
var=1
if var==1:
    print("你的数字错了1")
elif var==2:
    print("你的数字错了")
elif var==3:
    print('你的数字错了')
else:
    print('你的数字对了')

var = 3
if var == 1:
    print('你的数字猜错了')
elif var == 2:
    print('你的数字猜错了 ',)
elif var == 3:
    print('你的数字猜错了 代码来到了这里')
elif var == 4:
    print('你的数字猜错了')
elif var == 5:
    print('你的数字猜错了')


#猜数字游戏
#不需要使用循环，只需要猜一次，对就对，不对就不对
#引用随机数库
# import random
# #生成一个随机函数
# num=random.randint(1,6)
# #输入数字
# numvar=int(input("请输入数字：")) #input函数输出的结果是字符串需要通过int进行类型转换
# if num==numvar:
#     print("答对了")
# else:
#     print("答错了")

# 输入3个数字a,b,c按大小顺序输出
# a = int(input('请输入第一个需要猜的数字'))
# b = int(input('请输入第二个需要猜的数字'))
# c = int(input('请输入第三个需要猜的数字'))
# if a > b > c:
#     print('排列的顺序是',a,b,c)
# elif a > c > b:
#     print('排列的顺序是',a,c,b)
# elif b > a > c:
#     print('排列的顺序是',b,a,c)
# elif b > c > a:
#     print('排列的顺序是',b,c,a)
# elif c > a > b:
#     print('排列的顺序是',c,a,b)
# elif c > b > a:
#     print('排列的顺序是',c,b,a)
# else:
#     print('系统错误')

#for if break continue的嵌套使用

listvar=['jason','cherry','sherry','peter']
#for 加 if break的嵌套 如果i的值等于'cherry'就不再循环
for i in listvar:   #遍历listvar 每次遍历的值赋予i
    print(i)        #打印遍历i的值
    if i=='cherry': #判断 i = 'cherry'
        break       #break 终止循环

#for 加 if continue的嵌套 如果i的值=='cherry' 就忽略不执行下面的代码
listvar=['jason','cherry','sherry','peter']
for i in listvar:   #遍历listvar 每次遍历的值赋予i
    if i =='cherry':    #判断 i = 'cherry'
        continue        #跳过本次执行的代码
    print(i)

#while if break continue的嵌套使用
# a=10
# b=20
# while a==10:    #while 后面接的条件为成立 为True 后面的代码才会执行
#     if b==20:   #if 判断b等于20 则break终止后面的代码 不打印print('b的值是',b)
#         break   #break终止后面的代码
#     print('b的值是',b)
#
# # continue 加 if continue的嵌套 如果b的值==20就忽略不执行下面的代码
# while a == 10:
#     if b == 20:
#        continue   #continue跳过后面的代码
#        print('b的值是', b)

# 猜数字的游戏 (猜10次)
# 猜对了就直接告诉我猜对了

# 引用随机数库
import random
#生成一个随机数
num=random.randint(1,6)
#输入数字
# numvar=int(input("请输入数字:")) #input函数输出的结果是字符串需要通过int进行类型转换
#定义次数
count=10
#定义剩余次数
cishu=10
while count>0:
    numvar = int(input("请输入数字:"))
    if num==numvar:
        print("答对了")
        break
    else:
        cishu=cishu-1
        print("答错了次数还有",cishu,"次")
    count-=1

# 用户为自己的账号充值
# 1、最多可以充值5次
# 2. 充值的次数的总共金额不可以超过500元
#定义账号金额
id=0
#定义可充值金额
money=500
#定义剩余充值次数
cishu=5
#定义总的充值次数
count=0
while count<5:
    var=int(input("请输入充值金额："))
    if var<=money:
        id=id+var
        money=money-var
        cishu=cishu-1
        print("当前账号额度：",id)
        print("当前剩余充值次数",cishu)
        print("当前剩余可充值金额",money)
    else:
        print("充值金额大于可充值金额",money)

    count+=1





