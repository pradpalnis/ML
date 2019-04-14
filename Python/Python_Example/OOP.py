# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:15:01 2019

@author: PP00495588
"""

# A simple example class 
class Test: 
	
	# A sample method 
	def fun(self): 
		print("Hello") 

# Driver code 
obj = Test() 
obj.fun() 


# A Sample class with init method 
class Person: 

	# init method or constructor 
	def __init__(self, name): 
		self.name = name 

	# Sample Method 
	def say_hi(self): 
		print('Hello, my name is', self.name) 

p = Person('Shwetanshu') 
p.say_hi() 


# Python program to show that the variables with a value 
# assigned in class declaration, are class variables and 
# variables inside methods and constructors are instance 
# variables. 

# Class for Computer Science Student 
class CSStudent: 

	# Class Variable 
	stream = 'cse'			

	# The init method or constructor 
	def __init__(self, roll): 
	
		# Instance Variable	 
		self.roll = roll	 

# Objects of CSStudent class 
a = CSStudent(101) 
b = CSStudent(102) 

print(a.stream) # prints "cse" 
print(b.stream) # prints "cse" 
print(a.roll) # prints 101 

# Class variables can be accessed using class 
# name also 
print(CSStudent.stream) # prints "cse"	 


# Python program to show that we can create 
# instance variables inside methods 

# Class for Computer Science Student 
class CSStudent: 
	
	# Class Variable 
	stream = 'cse'	
	
	# The init method or constructor 
	def __init__(self, roll): 
		
		# Instance Variable 
		self.roll = roll			 

	# Adds an instance variable 
	def setAddress(self, address): 
		self.address = address 
	
	# Retrieves instance variable	 
	def getAddress(self):	 
		return self.address 

# Driver Code 
a = CSStudent(101) 
a.setAddress("Noida, UP") 
print(a.getAddress()) 


# An empty class 
class Test: 
	pass
