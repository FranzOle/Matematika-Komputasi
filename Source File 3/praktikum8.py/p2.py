def f(x):
    return x + 2

def g(x):
    return 3 * x

def f_g(x):
    return f(g(x))

x = 4
print("f(g(x))=", f_g(x))