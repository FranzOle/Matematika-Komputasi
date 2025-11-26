def f(x):
    return 2 * x + 3

def f_inverse(y):
    return (y - 3) / 2

x = 10
y = f(x)

print("f(x)=", y)
print("f_inverse(y)=", f_inverse(y))