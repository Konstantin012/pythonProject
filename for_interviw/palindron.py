# name = "hello dear Konstantin"
# print(name[0])
# print(name[-1])
#
# def calcualte (one:str, two:str):
#     print(int(one)+int(two))
# calcualte("1","2")
#
# def calcualte2 (one:int):
#     print(one**2)
# calcualte2(6)

def palindron1(value:str):
    rever = value[::-1]
    print(rever)
    ln = len(value)
    for i in range(0,ln):
        if value[i]==rever[i]:
            return True
        else:
            return False

print(palindron1("1235321"))

def palindron2(value:str):
    ret = True
    ln = len(value)
    for i in range(0,ln):
        a =value[i]
        b =value[-(i+1)]
        if value[i]==value[-i]:
            ret =True
        else:
            ret =False
    return ret

print(palindron2("1235327"))