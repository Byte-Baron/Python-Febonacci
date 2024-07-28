print("\n" * 40)
def f(n):
    if n <= 1:
        return n
    else:
        f_list = [0, 1]
        while len(f_list) < n:
            f_list.append(f_list[-1] + f_list[-2])
        return f_list

z=int(input("Enter a number : "))
print(f(z))
