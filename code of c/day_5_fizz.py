
for kid in range(1,10):
    kid = int(input("Enter a number "))
    if kid % 3 == 0 and kid % 5 == 0:
        print("FIzzBuzz")
    elif kid % 3 == 0:
        print("fizz")
    elif kid %5 == 0:
        print("Buzz")
    else:
        print(kid)