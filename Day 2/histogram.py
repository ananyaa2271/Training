
def frequency(l):
    result = dict()
    l.sort()

    x = l[0]
    count=1

    for i in l: 
        if i != x:
            count = 1
            x = i
        result[str(x)] = count
        count+=1
    
    return result

def make_graph(k, v):
    print(f'{k} |{"="*v} {v}')

def histogram(f):
    for i in f:
        make_graph(i, f[i])
        
            
l = [int(x) for x in input("Enter Sequence: ").split(' ')]
print("\n--- Histogram ---")
f = frequency(l)
histogram(f)

print()



