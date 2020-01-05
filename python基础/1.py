strvar = 'fasjdfjka21jsn3jsdsd7kdn9k8nc'
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