''' Q1. Define a variable of all the labours and print the name of each labour.
Condition:-
    Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh
    labour variable should be something like this 1st_labour, 2nd_labour and so on.'''

labour1 = "Mahesh"
labour2 = "Mithilesh"
labour3 = "Ramesh"
labour4 = "Sumesh"

print(labour1, labour2, labour3, labour4)


''' Q2. Define a variable of all the labours daily wage and print the name and wage of each labour.
Condition:-
    Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh and wages are 500,400,400,300 respectively
    labour variable should be something like this 1st_labour_name,1st_labour_wage, 2nd_labour_name,
    2nd_labour_wage and so on.
    You are bound to use string formatting'''

labour1_wage = 500
labour2_wage = 400
labour3_wage = 400
labour4_wage = 300

print(f"1st labour name is {labour1} and wage is {labour1_wage}")
print(f"2nd labour name is {labour2} and wage is {labour2_wage}")
print(f"3rd labour name is {labour3} and wage is {labour3_wage})")


''' Q3. I want to print this paragraph and its line number from which this paragraph is printing
    """ Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
    we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
    help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
    we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
            I have to print this paragraph as it is given here.""" 

    Condition:- 
    You can't use triple quote.
    Triple quote at starting is also a part of paragraph. '''
 
from loguru import logger
logger.info(f"""
\"\"\" Programming aasan hai. We are gopiing to learn this in depth. While learning we have to make sure that
    we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
    help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
    we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
            I have to print this paragraph as it is given here.\"\"\"
""")
 

''' Q4. When do we get NameError? 

    Ans. NameError in Python occurs when you try to use a variable, function, 
         or object that has not been defined or is not accessible in the current scope.

'''

''' Q5. Python is a high level language. What does that mean by high level? 

   Python is a high-level language, it means that Python is designed to be closer to human
   language and farther from the machine language that computers understand. High-level 
   languages prioritize simplicity and abstraction to make programming more accessible and
   productive for humans.
'''


''' Q6. What is compiled and Inetrpreted language, list a few? 
    Ans. A compiled language is one in which the source code is translated into machine 
    code by a compiler before it is executed. The machine code is then directly executed
    by the computer's hardware.

    eg- C, C++, Java
    
    An interpreted language is one where the source code is executed line-by-line by an 
    interpreter at runtime. No separate compilation step is involved.

    eg- Python, JavaScript
'''

''' Q7. Get all varibales address from RAM and you find if something is similar? 

   Ans. In Python, you can access the memory address of a variable using the id() function. 
        This function returns the memory address of the object the variable refers to. 
        If two variables have the same memory address, they are referencing the same object in memory.

'''
