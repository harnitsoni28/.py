from loguru import logger

# List -> Collection of similar and different data type

# list1 = [1, "Herry", 2.5, True]

labour_total = ["Ramesh", "Mahesh", "Mithilesh", "Sumesh"]

logger.info(f"{labour_total[3]}")

labour_total.append("Ram")  # append use for add element in list and add only one element  
labour_total.append("Mohan")

logger.info(f"{labour_total[5]}")

new_labour =["Ram", "Mohan"]
labour_total.extend(new_labour) # .extend() use for multiple element storing in the List 
logger.info(f"{labour_total}")


# labour_total.append(new_labour)
# logger.info(f"{labour_total}") # o/p-  ['Ramesh', 'Mahesh', 'Mithilesh', 'Sumesh', 'Ram', 'Mohan', ['Ram', 'Mohan']]  - Hence we will not use append in list



labour_total.insert(2, "Herry")  # .insert() use to insert at any index 
logger.info(f"{labour_total}")

logger.info(f"{labour_total[-1]}") # Neg indexing acess the last element of list

labour_wage = [["Mahesh", 500], ["Ramesh", 400]]  # Multi-Dimension Array [[_,_]]
print(labour_wage[0][1])
logger.info(f"Labour {labour_wage[1][0]} is charging total of {labour_wage[1][1]} per day")

