#sort a dictionary by value
a = {"a":12, "b":23, "c":6, "d":91, "e":45}
a = sorted(a.values())
print(a)

# keys are from 1 to 15 and value are their square number
a= {}
for i in range(1,16):
    a[i] = i*i

print(a)

#multiply all items
a = {"a":12, "b":23, "c":6, "d":91, "e":45}
b = 1
for i in a:
    b *=a[i]
print(b)

#sort a dictionary by keys
a = {"a":12, "b":23, "c":6, "d":91, "e":45}
a= sorted(a.keys())
print(a)

#program to find max and min value in sets
a = {34,5,64,8,9}
maximum = max(a)
minimum = min(a)
print("the max value in a is ", maximum)
print("the min value in a is ", minimum)

# common element in 3 lists using sets
a = [1,2,3,4,5,6]
b = [3,4,7,8,5,]
c = [3,4 ,5,6,3,]

print(set (a) & set (b) & set (c))

# to find difference between two sets
a = {1,2,3,4,5,6}
b = {3,4,7,8,5,}
x = a.difference(b)
print(x)

#to remove an item from set if it lies in set
a = {1,2,3,4,5,6}
a.remove(1)
print(a)

#check a set is subset of another set
a = {1,2,3,4,5,6,7}
b = {3,4,7,5}
print(b.issubset(a))
