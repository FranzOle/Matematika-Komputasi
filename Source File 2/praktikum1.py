from itertools import chain, combinations

def power_set(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

set_a = {1, 2, 3}
print(power_set(set_a))

set_a = {1,2, 3}
set_b = {4, 5, 6}
# print(len(set_a) == len(set_b))

# print(set_a.isdisjoint(set_b))

