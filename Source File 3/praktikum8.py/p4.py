def identity(x):
    return x

def constant(c):
    def f(x):
        return c
    return f

def absolute_value(x):
    return abs(x)

x_values = [-10, 0, 10]

print("Fungsi Identitas:")
for x in x_values:
    print(f"identity({x}) =", identity(x))

print("\nFungsi Konstan (c = 7):")
constant_func = constant(7)
for x in x_values:
    print(f"constant(7)({x}) =", constant_func(x))

print("\nFungsi Nilai Mutlak:")
for x in x_values:
    print(f"absolute_value({x}) =", absolute_value(x))