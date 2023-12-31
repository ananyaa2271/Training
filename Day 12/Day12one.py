import time

 

def cached(fun):

    fact_dict = dict()

    def inner(x):

        if x in fact_dict.keys():

            print("**"*50)

            print(f'factorial of {x} alredy in the cache')

            print(fact_dict[x])

            return fact_dict[x]

        else:

            print("**"*50)

            print("not in the cache")

            result = fun(x)

            print(result)

            fact_dict[x] = result

            return result

    return inner

 

def performance_log(fun):

    def inner(num):

        start = time.time()

        result = fun(num)

        end = time.time()

        print(f'factorial of {num}: {result}')

        print(f'this {fun.__name__} takes {end-start} sec')

        return result

    return inner

 

@cached

@performance_log

def factorial(x):

    fact = 1

    for i in range(1, x + 1):

        fact = fact * i

    return fact

for i in range(1,5):

    factorial(i)

factorial(4)

#cached(performane_log(cached))

