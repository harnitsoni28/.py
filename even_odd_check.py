from loguru import logger

number = int(input("Enter the Number: "))

if(number % 2 == 0):
    logger.info(f"This is Even Number")
else:
    logger.info("This is Odd Number") 