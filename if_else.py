a = 5
print (a>5)
print (a>=5)
 

from loguru import logger

length_of_land = 100
bredth_of_land = 200
bricks_cost_per_peice = 10.5
laboure_mistri1 = "Jagmohan"
laboure_mistri2= "Rampyare"
is_home = True

length_of_land = int(input("Enter the length of your land : "))

if (length_of_land < 100):
    logger.info(f"Your length is not sufficient to buid 4 BHK")
    if length_of_land > 80:
        logger.info(f"You can build 3 BHK house")
    else:
        logger.info("You don't have enough space")

elif length_of_land >= 500:
    logger.info(f"You can build more than two buildings")    
else:
    logger.info(f"Share more details with us")


    