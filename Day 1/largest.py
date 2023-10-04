'''def largest(l):
    max = -999999
    for i in l:
        if i>max:
            max = i
    return max

def second_largest(l, max):
    second_max = -999999
    for i in l:
        if i > second_max and i < max:
            second_max = i
    return second_max

input = input('Enter n numbers : ').split(' ')
l = [int(x) for x in input]

max = largest(l)
second_max = second_largest(l, max)

print("Largest Number = ", max)
print("Largest Number = ", second_max)
'''



n = int(input("Enter n: "))
max = None
second_max = None

for i in range(n):
    print(f"Enter number {i+1}: ", end="")
    x = int(input())
    if max == None:
        max = x
        print("if")
    elif x>max:
        print("else if")
        second_max = max
        max = x
    elif second_max == None:
        second_max = x
        print("elif")
    elif x > second_max:
        print("else elif")
        second_max = x
    

print("Largest Number = ", max)
print("Second Largest Number = ", second_max)