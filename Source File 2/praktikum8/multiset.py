from collections import Counter

def multiset_count(elements):
    count = Counter(elements)
    return count

students = ['Alya', 'Alya', 'Budi', 'Deny', 'Deny', 'Deny']
print(multiset_count(students))
