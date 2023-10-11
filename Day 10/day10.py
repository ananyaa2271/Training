class PrimeIterator:

    def __init__(self, max, min=0):

        self.min = min

        self.max = max

     

 

    def prime_check(self,number):

        if number>1:

            for i in range(2, (number//2)+1):

                if number % i == 0:

                    return False

            return True

        else:

            return False

       

    def __iter__(self):

        return self

   

    def __next__(self):

        while self.min <= self.max:

            if self.prime_check(self.min):

                prime = self.min

                self.min+=1

                return prime

            self.min +=1

        raise StopIteration

   

def main():

    for number in PrimeIterator(10):

        print(number)

main()