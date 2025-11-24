A = {1, 2, 3}
B = {2, 4, 6}

relation = [(a, b) for a in A for b in B if b % a == 0]
print("Relasi R:\n", relation)

def is_reflexive (relation, set_a):
    return all((a, a) in relation for a in set_a)

print("Apakah relasi refleksif?", is_reflexive(relation, A))