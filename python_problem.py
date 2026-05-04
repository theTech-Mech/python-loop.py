# fibonacci series up to 10 number
a=0
b=1

print(a)
print(b)
for i in range(2,11):
    c=a+b
    a=b
    b=c
    print(c)

# input from user in fibonacci series
a=0
b=1
num=int(input("enter the number"))
if num<=1:
    print("number is not prime number")
else:
print(a)
print(b)
for i in range(2,11):
    c=a+b
    a=b
    b=c
    print(c)



# prime number or not
num=int(input("Enter a number: "))

if num<=1:
    print("number is not prime number")
else :
    for i in range (2,num):
        if num%i==0:
            print("number is not prime number")
            break
        else:
            print("number is prime number")


# check palindrome or not
num = int(input("Enter a number: "))
tem = num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10

   if rev==tem:
       print("number is palindrome number")
   else:
       print("number is not palindrome number")
       
