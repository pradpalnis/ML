# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:39:30 2019

@author: PP00495588
"""

# Python program to illustrate destructor 
class Employee: 

	# Initializing 
	def __init__(self): 
		print('Employee created.') 

	# Deleting (Calling destructor) 
	def __del__(self): 
		print('Destructor called, Employee deleted.') 

obj = Employee() 
del obj 


# Python program to illustrate destructor 

class Employee: 

	# Initializing 
	def __init__(self): 
		print('Employee created') 

	# Calling destructor 
	def __del__(self): 
		print("Destructor called") 

def Create_obj(): 
	print('Making Object...') 
	obj = Employee() 
	print('function end...') 
	return obj 

print('Calling Create_obj() function...') 
obj = Create_obj() 
print('Program End...') 
