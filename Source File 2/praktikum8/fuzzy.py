def fuzzy_union(fuzzy_set_a, fuzzy_set_b):
    return {k: max(fuzzy_set_a.get(k, 0), fuzzy_set_b.get(k, 0)) for k in set(fuzzy_set_a) | set(fuzzy_set_b)}

def fuzzy_intersection(fuzzy_set_a, fuzzy_set_b):
    return {k: min(fuzzy_set_a.get(k, 0), fuzzy_set_b.get(k, 0)) for k in set(fuzzy_set_a) & set(fuzzy_set_b)}

def fuzzy_complement(fuzzy_set):
    return {k: 1 - v for k, v in fuzzy_set.items()}

fuzzy_matkom = {'Deny': 0.7, 'Budi': 0.5, 'Chandra': 0.9}
fuzzy_strukdat = {'Deny': 0.6, 'Budi': 0.8, 'Chandra': 0.4}

union_result = fuzzy_union(fuzzy_matkom, fuzzy_strukdat)
intersection_result = fuzzy_intersection(fuzzy_matkom, fuzzy_strukdat)
complement_result = fuzzy_complement(fuzzy_matkom)

print(f"Union Fuzzy: {union_result}")
print(f"Intersection Fuzzy: {intersection_result}")
print(f"Complement Fuzzy Matkom: {complement_result}")