
if temp < 32:
    print("ice")
elif temp < 212:
    print("water")
else:
    print("steam")


x = 1
if x > 3:
    if x > 4:
        print("A", end=" ")
    else:
        print("B", end=" ")
elif x < 2:
    if x != 0:
        print("C", end=" ")
    print("D")


weather = "raining"
if weather == "sunny":
    print("wear sunblock")
elif weather == "snow":
    print("going skiing")
else:
    print(weather)


if int("zero") == 0:
    print("zero")
elif str(0) == '0':
    print(0)
else:
    print("none of the above")


if n == 0:
    print("zero")
elif n == 1:
    print("one")
elif n == 2:
    print("two")
else:
    print("three")


n = int(input("Enter an integer: "))
if n < 0:
    print("invalid value")
else:
    for i in range(1, n + 1):
        print(i * i)


n = int(input("Enter an integer: "))
if n < 1:
    print("invalid value")
else:
    for i in range(1, n + 1):
        print(i * i)


n = int(input("Enter an integer: "))
if n > 0:
    for a in range(1, n + n):
        print(a / (n / 2))
else:
    print("Now quitting")

n = int(input("Enter an integer: "))
if n > 0:
    for a in range(1, n + n):
        print(a / (n / 2))
else:
    print("Now quitting")


i = 100
while (i > 0):
    print(i)
    i -= 3

while num > 0:
    print(num % 10)
    num = num // 10

while num > 0:
    count += 1
    sum += num
    num -= 2
    if count == 10:
        print(sum / float(count))
        break


min = 0
max = num
if num < 0:
    min = num
    max = 0  
for i in range(min, max + 1):
    sum += i


count = 0
while count < 10:
    print("Hello")
    count += 1

x = 10
y = 0
while x > y:
    print(x, y)
    x -= 1
    y += 1

keepgoing = True
x = 100
while keepgoing:
    print(x)
    x -= 10
    if x < 50:
        keepgoing = False

x = 45
while x < 50:
    print(x)

for x in [1, 2, 3, 4, 5]:
    print(x)

for x in range(5):
    print(x)

for p in range(1, 10):
    print(p)

for q in range(100, 50, -10):
    print(q)

for z in range(-500, 500, 100):
    print(z)

for y in range(500, 100, 100):
    print("*", y)

x = 10
y = 5
for i in range(x - y * 2):
    print("%", i)

for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        print(x, y)

for x in range(3):
    for y in range(4):
        print(x, y, x + y)

c = 0
for x in range(10):
    for y in range(5):
        c += 1
print(c)


for i in range(4):
    for j in range(5):
        if i + 1 == j or j + i == 4:
            print("+", end=" ")
        else:
            print("o", end=" ")
    print()


while True:
    n = int(input("Enter an int: "))
    if n == A1:
        continue
    elif n == A2:
        break
    else:
        print("what")
else:
    print("ever")

while True:
    n = int(input("Enter an int: "))
    if n == A1:
        continue
    elif n == A2:
        break
    else:
        print("what")
print("ever")

while True:
    n = int(input("Enter an int: "))
    if n == A1:
        continue
    elif n == A2:
        break
print("what")
print("ever")