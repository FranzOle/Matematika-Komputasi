python_class = {'Alya', 'Deny', 'Chandra', 'Diana'}
java_class = {'Deny', 'Diana', 'Eka', 'Farhan'}
cpp_class = {'Alya', 'Farhan', 'Gilang'}
union_students = python_class.union(java_class, cpp_class)
intersection_students = python_class.intersection(java_class, cpp_class)
difference_students = python_class.difference(java_class.union(cpp_class))

print(f"Gabungan Siswa {union_students}")
print(f"Siswa yang mengikuti ketiga kelas: {intersection_students}")
print(f"Siswa yang hanya mengikuti Kelas Python: {difference_students}")