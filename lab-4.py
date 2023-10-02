# Task-1
"""
# Get user input
user_input = input("Enter a string without whitespaces: ")

# Initialize an empty tuple
result_tuple = ()

# Iterate through the characters of the input string and append them to the tuple
for char in user_input:
    result_tuple += (char,)

# Print the created tuple
print("Created tuple is:")
print(result_tuple)
"""
# Task-2
"""
# Sample Input (tuple)
input_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')

# Convert the tuple to a string using the join method
result_string = ''.join(input_tuple)

# Print the resulting string
print("The string is:", result_string)
"""
# Task-3
"""
# Sample Input
tuple_A = (1, 2, 3, 4, 5, 6, 7)
tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)

# Calculate the lengths of the two tuples
len_A = len(tuple_A)
len_B = len(tuple_B)

# Calculate the midpoint index for tuple_A
midpoint = len_A // 2

# Concatenate the first half of tuple_A with the second half of tuple_B
result_tuple = tuple_A[:midpoint] + tuple_B[midpoint:]

# Print the resulting concatenated tuple
print(result_tuple)
"""
# Task-4
"""
# Sample Input
input_tuple_1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
input_tuple_2 = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)
input_tuple_3 = ((1, 2, 3), (['A', 'B']), (1, 2, 3), (['A']))

# Function to count element occurrences and create pairs
def count_element_occurrences(input_tuple):
    element_count = {}
    for element in input_tuple:
        if isinstance(element, list) or isinstance(element, tuple):
            element = tuple(element)
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    element_occurrences = [(key, value) for key, value in element_count.items()]
    return element_occurrences

# sample output
output_tuple_1 = count_element_occurrences(input_tuple_1)
output_tuple_2 = count_element_occurrences(input_tuple_2)
output_tuple_3 = count_element_occurrences(input_tuple_3)

# Print the resulting tuples
print("Elements and their occurrences (Sample 1):")
print(output_tuple_1)

print("\nElements and their occurrences (Sample 2):")
print(output_tuple_2)

print("\nElements and their occurrences (Sample 3):")
print(output_tuple_3)

"""
# Task-5
"""
# sample Input
input_data = (55, 6, 777, 70.0, '7', 'A')

# initialize empty tuples
int_tuple = ()
float_tuple = ()
str_tuple = ()

# Iterate through  input data
for item in input_data:
    if isinstance(item, int):
        int_tuple += (item,)
    elif isinstance(item, float):
        float_tuple += (item,)
    elif isinstance(item, str):
        str_tuple += (item,)

# print resulting tuples
print(int_tuple)
print(float_tuple)
print(str_tuple)
"""
# Task-6
"""
# Get user input
user_input = input("Enter a string without whitespaces: ")

# Create a set using set comprehension to remove whitespaces
result_set = {char for char in user_input}

# Print the created set
print("Created set is:")
print(result_set)
"""
#Task-7
"""
set_X = {1,2,3,4,5}
set_Z = {5,7,8,9,2,10}
difference_set = set_X.symmetric_difference(set_Z)
print(difference_set)
"""

#Task-8
"""
set_X = {1,2,3,4,5}
set_B = {5,7,8,9,2,10}
set_X.difference_update(set_B)
print(set_X)
"""

#Task-9
"""
set_a = {1, 2, 3, 4, 7}
set_b = {8, 7, 9, 4, 2, 0, 10}
set_c = {4, 0, 1}
for element in set_c:
    if element in set_a:
        set_a.remove(element)
        set_b.add(element)
print(set_a)
print(set_b)

"""
#Task-10
"""
from itertools import combinations
a = {1,2,3,4,5,6}
n = 3
m = 5
combinations_set = list(combinations(a, n))
selected_combinations = combinations_set[:m]
result_list = [set(comb) for comb in selected_combinations]
print(result_list)
"""

#Task-11
"""
from itertools import groupby
cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'),
             ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]
cars_list.sort(key=lambda x: x[0])
for key, group in groupby(cars_list, key=lambda x: x[0]):
    print(f"{key} {len(list(group))}")
    for car in group:
        print(f"- {car[1]}")

"""
#Task-12+bonus
"""
data = (5, 55, 10, 1, 0, 1, 55, 77, 10, 5, 5, 55, 77)
from collections import Counter
counter = Counter(data)
items = list(counter.items())
max_occurrence = max(counter.values())
min_occurrence = min(counter.values())
most_popular = [item for item in items if item[1] == max_occurrence]
least_popular = [item for item in items if item[1] == min_occurrence]
frequent_occurrences = Counter(counter.values())
frequent_values = [value for value, count in frequent_occurrences.items() if count > 1]
frequent_elements = [item for item in items if item[1] in frequent_values]
print(tuple(items))
print("The most p element:", end=" ")
if len(most_popular) > 1:
    print("no most p element")
else:
    print(most_popular[0])
print("The least p element:", end=" ")
if len(least_popular) > 1:
    print("no least p element")
else:
    print(least_popular[0])
print("The frequent elements:", end=" ")
print(tuple(frequent_elements))
"""