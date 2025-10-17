def verify_proposition(a, b):
    union_result = a.union(b)
    intersection_result = a.intersection(union_result)

    return intersection_result == a

a = {2, 4, 6}
b = {4, 6, 8}

print(verify_proposition(a, b))  

