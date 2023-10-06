import time

 

def performance_log(find_prime):

    def inner(min, max):

        start=time.time()

        result=find_prime(min,max)

        print(f'Prime numbers are {result}')

        end=time.time()

        print(f'Total time taken to list the prime numbers is {end-start}')

    return inner

 

 

@performance_log

def find_prime(min, max):

    primes=[]

    for i in range(min, max+1):

        if i>1:

            for j in range(2, i):

                if (i%j) == 0:

                    break

            else:

                primes.append(i)

        else:

            i=i+1

    return primes

 

find_prime(2,100)

# performance_log(find_prime)(2,200)

 

# x = find_prime(2,50000)