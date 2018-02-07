test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = []
odd_nums = []

print (sum(test_list[0:]))

print(max(test_list[0:]))

print(min(test_list[0:]))

for number in test_list[0:]:
    if number % 2 == 0:
        even_nums.append(number)
    else:
        odd_nums.append(number)
print(even_nums[0:])
print(odd_nums[0:])

second_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
pos_nums = []

for number2 in second_list[0:]:
    if number2 > 0:
        pos_nums.append(number2)
print(pos_nums[0:])

multi_list = []
for numba in second_list[0:]:
    multi_list.append(numba * 2)
print(multi_list[0:])

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = [list1*list2 for list1, list2 in zip(list1, list2)]
print(list3)


import numpy as np
mat1 = np.matrix([
    [1, 3],
    [2, 4]
])
mat2 = np.matrix([
    [5, 2],
    [1, 0]
])
print(mat1 + mat2)

mat3 = np.matrix([
    [1, 3, 9],
    [2, 4, 6]
])
mat4 = np.matrix([
    [5, 2, 5],
    [1, 0, 3]
])
print(mat3 + mat4)

checkit = ["test", "these", "and", "these", "and", "these"]
print(checkit)
print("Now clean it up:")
checkit = set(checkit[0:])
print(checkit)