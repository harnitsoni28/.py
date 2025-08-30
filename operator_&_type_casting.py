from loguru import logger

length_of_land = 100
bredth_of_land = 200
bricks_cost_per_peice = 10.5
laboure_mistri1 = "Jagmohan"
laboure_mistri2= "Rampyare"
is_home = True

# calulate total area of land
 
total_area_of_land = length_of_land * bredth_of_land

perimeter_of_land = 2*(length_of_land + bredth_of_land)

logger.info(f"Total area of land is {total_area_of_land}")

logger.info(f"Perimeter of land is {perimeter_of_land}")

# Modulo operator

# print(15%6)                      # use in armstrong number


print(15//7)       # floor division

import math
print(math.ceil(15/7))
print(math.floor(15/7))


a = "Herry" 
b= "2"

print(a+b)          # adding two string = Concatention

c= 23

print(int(b)+c)     # typecasting is basicaly cast data type acc to need  
print(a+str(c))


d= 10
e = 12.5
print(d+e)      # 22.5  implicit typecasting -> Python does it by own

length_of_the_land = int(input("Please enter the length of Land: "))   # Alwasys define data type for input
bredth_of_the_land = float(input("Please enter the bredth of Land: "))

total_area_of_the_land = (length_of_the_land * bredth_of_the_land)

logger.info(f"Total area of the Land {(total_area_of_the_land)} sq ft")
logger.info(f"Total area of the Land {abs(total_area_of_the_land)} sq ft") # abs() is used for positive o/p result they skip negative part
