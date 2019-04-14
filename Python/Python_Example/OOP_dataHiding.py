# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:24:14 2019

@author: PP00495588
"""

class MyClass: 

	# Hidden member of MyClass 
	__hiddenVariable = 0
	
	# A member method that changes 
	# __hiddenVariable 
	def add(self, increment): 
		self.__hiddenVariable += increment 
		print (self.__hiddenVariable) 

# Driver code 
myObject = MyClass()	 
myObject.add(2) 
myObject.add(5) 

# This line causes error 
print (myObject.__hiddenVariable) 


# A Python program to demonstrate that hidden 
# members can be accessed outside a class 
class MyClass: 

	# Hidden member of MyClass 
	__hiddenVariable = 10

# Driver code 
myObject = MyClass()	 
print(myObject._MyClass__hiddenVariable) 


class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	def __repr__(self): 
		return "Test a:%s b:%s" % (self.a, self.b) 

	def __str__(self): 
		return "From str method of Test: a is %s," \ 
			"b is %s" % (self.a, self.b) 

# Driver Code		 
t = Test(1234, 5678) 
print(t) # This calls __str__() 
print([t]) # This calls __repr__() 


class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	def __repr__(self): 
		return "Test a:%s b:%s" % (self.a, self.b) 

# Driver Code		 
t = Test(1234, 5678) 
print(t) 


class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

# Driver Code		 
t = Test(1234, 5678) 
print(t) 
