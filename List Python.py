q=[]
a=[1, 2, 3]
z=[1, 2.5, 3.7, 9]
x=['a','b','c']
c=['a', 1, 'b', 3.5, 'zero']
s=['One', 'Two', 'Three']

[2, 4, 6,]
['abc', 'def']
[1, 2.0, 3, 4.0]
[]

L=[]
L=[value, ...]

L=list()
sqrs=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169,
      196, 225]

l1=list(input('Enter list elements:'))

L=list(<sequence>)

lst=eval(input("Enterlist:"))
length=len(lst)
min_ele=lst[0]
min_index=0
for i in range(1, length):
    if lst[i]<min_ele:
        min_ele=lst[i]
        min_index=i
print("Given list is:", lst)
print("The minimum element of the given lisr is:")
print(min_ele, "at index", min_index)

lst=eval(input("Enterlist:"))
length=len(lst)
mean=sum=0
for i in range(0, length)