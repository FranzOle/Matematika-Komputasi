def is_valid_partition(original_set, partition):
    combined = set()
    for part in partition:
        combined.update(part)
    if combined == original_set and all(len(part) > 0 for part in partition):
        return True, f"Benar ini merupakan partisi"
    return False

original_set = {'Adam', 'Bella', 'Charlie', 'Deny', 'Eko', 'Farid'}
partition = [{'Adam', 'Bella', 'Charlie'}, {'Deny', 'Eko', 'Farid'}]
print(is_valid_partition(original_set, partition))

