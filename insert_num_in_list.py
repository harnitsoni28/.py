# Q. Insert number in such a way that list is sorted in Descending order 

lst = [202, 165, 89, 76, 12]
number_to_insert = 15
index = 0

# Find the correct index for insertion
for num in lst:
    if num < number_to_insert:
        break
    index += 1

# Append a placeholder to expand the list
lst.append(None)

# Shift elements to make room for the new number
for i in range(len(lst) - 1, index, -1):
    lst[i] = lst[i - 1]

# Insert the new number at its correct position
lst[index] = number_to_insert  

print(lst) 

