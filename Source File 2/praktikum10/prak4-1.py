def fuzzy_union(fuzzy_set_a, fuzzy_set_b):
    return {k: max(fuzzy_set_a.get(k, 0), fuzzy_set_b.get(k, 0)) for k in set(fuzzy_set_a) | set(fuzzy_set_b)}

def fuzzy_intersection(fuzzy_set_a, fuzzy_set_b):
    return {k: min(fuzzy_set_a.get(k, 0), fuzzy_set_b.get(k, 0)) for k in set(fuzzy_set_a) & set(fuzzy_set_b)}

def fuzzy_complement(fuzzy_set):
    return {k: 1 - v for k, v in fuzzy_set.items()}

fuzzy_math = {'Edo': 0.9, 'Rina': 0.7, 'Tari': 0.8}
fuzzy_physics = {'Edo': 0.6, 'Rina': 0.9, 'Tari': 0.5}

union_result = fuzzy_union(fuzzy_math, fuzzy_physics)
intersection_result = fuzzy_intersection(fuzzy_math, fuzzy_physics)
complement_result = fuzzy_complement(fuzzy_math)

print(f"Union Fuzzy: {union_result}")
print(f"Intersection Fuzzy: {intersection_result}")
print(f"Complement Fuzzy Matematika: {complement_result}")