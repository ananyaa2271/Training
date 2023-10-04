def prime(min, max):
    all_primes = list()
    primes = list()

    for i in range(2, max+1):
        flag = True

        for j in all_primes:
            if i%j == 0:
                flag = False
                break
        if flag:
            all_primes.append(i)
            if i>=min:
                primes.append(i)
    return primes


min = int(input("Enter Min of Range: "))
max = int(input("Enter Max of Range: "))

print("Primes between the range : ", prime(min, max))

