


length_of_land = 100
bricks_cost_per_peice = 10.5
laboure_mistri = "Jagmohan"
is_home = True

if length_of_land == 100:
   length_of_land = 200
else:
   length_of_land = 300

# print(length_of_land, bricks_cost_per_peice, laboure_mistri, is_home)

print("Name of Labour is", laboure_mistri)                        # (" for string ") 
print('Coast of brick per peice is', bricks_cost_per_peice)       # (' for string ') 
print('''My building is 4 BHK in
New Delhi, (India)''')                    # (''' for multiline string''') or \n


print("My building is '4 BHK' ")      # if use " " in starting then in middle we can use this for ' ' or vice versa
print('My building is "4 BHK" ')
print("My building is \"4 BHK\" ")   #for using double " " in one we use \ \
print("My building is \t \"4 BHK\" ")  # \t is use for change tab

 
# String Formatting :-

# f string and, .format method

print(f"cost of brick per unit is {bricks_cost_per_peice} ")

print("cost of brick per unit is {}".format(bricks_cost_per_peice))


# logging is use to know the line number - learn for debugging
from loguru import logger
logger.info(f"cost of brick per unit is {bricks_cost_per_peice} ")
logger.info(f' """cost of brick per unit is {bricks_cost_per_peice}""" ')
