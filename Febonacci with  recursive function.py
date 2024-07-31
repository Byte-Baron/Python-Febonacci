print("\n" * 40)
def f(n):
    if n <= 0:
        return "Input should be a number greater than 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        f_list = [""]
        f_list[0] += (f(n-1) + f(n-2))
        return f_list

z=int(input("Enter a number : "))
print(f(z))

