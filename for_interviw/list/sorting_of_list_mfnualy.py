a = ['23','12','13','17','23','19']
def doSomething(values):
    for i in range(1, len(values)):
        print(values[i])
        print(values[i - 1])
        if values[i] < values[i - 1]:
            t = values[i]
            values[i] = values[i - 1]
            values[i - 1] = t
            print(values)


doSomething(a)

b = 1;
while(b<=4):
    b*=2
print(b)