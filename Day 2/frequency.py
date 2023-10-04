
def frequency(l):
    result = dict()
    l.sort()

    x = l[0]
    count=1

    for i in l: 
        if i != x:
            count = 1
            x = i
        result[x] = count
        count+=1
    
    return result
            
l = [int(x) for x in input("Enter Sequence: ").split(' ')]
print("\n--- Frequency ---")
print(frequency(l))

print()

