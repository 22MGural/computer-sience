
#1
a=int(input('first number:'))
b=int(input('second number:'))
c=int(input('third number:'))
plus=(-b+(b**2-4*a*c)**0.5)/2*a
minus=(-b-(b**2-4*a*c)**0.5)/2*a
print(minus)
print(plus)

#2
a=int(input('first number:'))
b=int(input('second number:'))
c=int(input('third number:'))
if a>b and a>c:
    print('a is the biggeset')
elif c>b and c>a:
    print('c is the biggest')
elif b>a and b>c:
    print('b is the biggest')
  
#3 i)
for number in range (2,51,2):
    print(number)
#ii)
for number in range (1,51):
    if number %2 == 0:
        print(number)
        
#4
n=int(input('enter a number:'))
sum_of_series=n*(n+1)//2
print(sum_of_series)

#5
