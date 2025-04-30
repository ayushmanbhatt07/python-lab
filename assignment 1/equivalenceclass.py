# Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of
# numbers. Check the validity of your equivalence classes. [Hint: the union of all equivalence
# classes should be the original set/list.]
def create_equivalence_classes():
    equivalence_classes = {i: [] for i in range(5)}
    for num in range(1, 10001):
        equivalence_classes[num % 5].append(num)
    return equivalence_classes

def check_validity(equivalence_classes):
    all_numbers = []
    for key in equivalence_classes:
        all_numbers.extend(equivalence_classes[key])
    return sorted(all_numbers) == list(range(1, 10001))

equivalence_classes = create_equivalence_classes()
is_valid = check_validity(equivalence_classes)

print("Equivalence Classes:", equivalence_classes)
print("Is Valid:", is_valid)