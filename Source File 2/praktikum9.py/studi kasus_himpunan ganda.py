from collections import Counter

def multiset_count(elements):
    count = Counter(elements)
    return count

foods = ['Nasi Goreng', 'Nasi Goreng', 'Sate', 'Sate', 'Sate', 'Soto']
print(multiset_count(foods))