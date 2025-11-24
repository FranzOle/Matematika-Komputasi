A = {1, 2, 3}
B = {2, 4, 6}

relation = {(1, 2), (2, 4), (3, 6)}

def create_relation_table(set_a, set_b, relation):
    table = [[1 if (a, b) in relation else 0 for b in set_b] for a in set_a]
    return table

table = create_relation_table(A, B, relation)

for row in table:
    print(row)