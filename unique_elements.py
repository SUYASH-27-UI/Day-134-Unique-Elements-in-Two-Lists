list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

unique = []

for number in list1:
    if number not in list2:
        unique.append(number)

for number in list2:
    if number not in list1:
        unique.append(number)

print("First list:", list1)
print("Second list:", list2)
print("Unique elements:", unique)
