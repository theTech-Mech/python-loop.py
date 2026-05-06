a = [ "ross", "rachel", "monica", "joe"]

#swap first and fourth element
a[0] , a[3]= a[3],a[0]
print(a)

#add a new value in second position
a.insert(1,"phoebe")
print(a)

# delete value from 3rd position
a.pop(2)
print(a)

b = [13, 7, 12, 10 ]

#multiply all numbers
mul = 1
for i in (b):
    mul *= i
    print(mul)

#largest and smallest number in list
b.sort()
print(b)

print("the largest number in the list : ", b[-1])
print("the smallest number in the list : ", b[0])
