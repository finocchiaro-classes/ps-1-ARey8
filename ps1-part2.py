def number_fun(a, b):
    print(f"You entered {a} and {b}")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} ** {b} = {a ** b}")
    print(f"{a} % {b} = {a % b}")

firstnum = (int)(input("Enter an integer between 10 and 100: "))
secondnum = (int)(input("Enter an integer less than 4: "))
number_fun(firstnum, secondnum)