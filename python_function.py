# function to find greater in three numbers

def maximum_num (val1, val2,val3):
    if val1 > val2 and val1 > val3:
        print (val1,"is the greater number")
    elif val2 > val3 and val2 > val1:
        print (val2,"is the greater number")
    else:
        print (val3,"is the greater number")
maximum_num(12,56,3)

#create and print a list of the square number between 1 to 30

def create_list():
    l = []
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())


# function that takes a number as parameter and check it is prime or not

def prime_num(num):
    if num == 1:
        print (num,"is the not prime number")
    elif num == 2:
        print (num,"is the prime number")
    if num >2:
        for i in range (2 , num ):
            if num % i == 0 :
                print (num,"is the not prime number")
                break
            else:
                print (num,"is the prime number")
                break
prime_num(11)

#function for the sum of all the numbers in a list

def add(number):
    total = 0
    for i in number:
        total += i
    return total
print(add([10,6,7,43,61]))

#using recursion sum all the number in a list

def add(number):
    if len(number) == 1:
        return (number[0])
    else:
        return ( number[0] ) + add( number[1:] )

print (add([10,6,7,43,61]))

#fibonacci series using recursion
def fib(n):
    if n==1:
        return (0)
    elif n==2:
        return (1)
    else:
        return (fib(n-1) + fib(n-2))
    
print(fib(10))

