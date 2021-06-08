def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial (num-1)


n = int(input("enter a number:"))
out = factorial(n)
print("factorial of {} is {}".format(n, out))
