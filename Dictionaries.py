# Dictionary is an unordered collection that stores data in key-value pairs.
# dic = {'key1': 'value1', 'key2': 'value2'} 2.

# Mutability: Dictionaries are mutable; you can change the values associated with keys or add new key-value pairs 3.
# Order: As of Python 3.7+, dictionaries maintain the order of insertion for keys 1 3.
# Duplicates: Dictionary keys must be unique; however, values can be duplicated 4.
# create a dictionary using the dict() function or by direct assignment with curly braces 2.


labour_with_cost = {"Ramesh":500, "Mahesh":400, "Mithilesh":300, "Sumesh":250}

labour_with_cost["Jagmohan"] = 1000
labour_with_cost["Rampyare"] = 800

# print(labour_with_cost)

# print(labour_with_cost.keys())  # o/p: dict_keys(['Ramesh', 'Mahesh', 'Mithilesh', 'Sumesh', 'Jagmohan', 'Rampyare'])
# print(labour_with_cost.values()) # o/p: dict_values([500, 400, 300, 250, 1000, 800])
# print(labour_with_cost.items()) # o/p: dict_items([('Ramesh', 500), ('Mahesh', 400), ('Mithilesh', 300), ('Sumesh', 250), ('Jagmohan', 1000), ('Rampyare', 800)])


for abc in labour_with_cost:
    print(abc)