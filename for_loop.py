from loguru import logger

labour_name = ["Ram", "Mahesh", "Mithilesh", "Sumesh"]

# for name in labour_name:
#     logger.info(name)

for i in range(len(labour_name)):
    logger.info(f"labour {i+1} name is {labour_name[i]}")  #checked range (4,4) for i variable 
 

