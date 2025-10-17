def verify_proposition(A,B):
    union_result = A.union(B)
    intersection_result = A.intersection(union_result)
    return intersection_result == A

A = {1,2,3}
B = {3,4,5}
print(verify_proposition(A,B))