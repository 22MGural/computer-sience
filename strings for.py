diddy = input("Enter a string: ")
for Q in diddy:
    if Q.isupper():
        print(Q.lower(), end="")
    elif Q.islower():
        print(Q.upper(), end="")
    else:
        print(Q, end="")