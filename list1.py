from loguru import logger

labour_name = ["Ramesh", "Mahesh", "Mithilesh", "Sumesh", 500, 400, 300, 200]

print (labour_name[0:]) 
print (labour_name[1:4]) # access list using colon (:)

# print (labour_name[::-1]) # for reverse list (::-1)

print (len(labour_name)) # for check how many element in the list #len()

print(labour_name.pop())
print(labour_name.pop(1))

# labour_name.remove(400)
# print(labour_name)

labour_total = ["Rame", "Mahesh", "Mithilesh", "Sumesh", 500, 400, 300, 200]

labour_total[0] = "Ramesh"
print(labour_total)

labour_total[0:3]= ["Ramesh", "Suresh", "Ganesh"]
print(labour_total)


api_endpoint = "https://portal.azure.com/VIMISTANCE/test-vm/subs_id/aexy-234-mns/getCredential"

new_api_list = api_endpoint.split("/")
print(new_api_list)
print(new_api_list[-1])     # [-1] to get the last element on the list
print(new_api_list[-2])     # [-2] to get the 2nd last element on the list

