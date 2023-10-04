def sum(*args):
    res = 0
    for i in args:
        res+=i
    return res

def avg(*args):
    return sum(*args)/len(args)

l = [1,2,3,4,5,6,7,8,9,10]

print(avg(*l))