# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:51:54 2019

@author: PP00495588
"""

# Python Program illustrate how 
# to overload an binary + operator 

class A: 
	def __init__(self, a): 
		self.a = a 

	# adding two objects 
	def __add__(self, o): 
		return self.a + o.a 
ob1 = A(1) 
ob2 = A(2) 
ob3 = A("Geeks") 
ob4 = A("For") 

print(ob1 + ob2) 
print(ob3 + ob4) 


# Python Program to perform addition 
# of two complex numbers using binary 
# + operator overloading. 

class complex: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	# adding two objects 
	def __add__(self, other): 
		return self.a + other.a, self.b + other.b 

	def __str__(self): 
		return self.a, self.b 

Ob1 = complex(1, 2) 
Ob2 = complex(2, 3) 
Ob3 = Ob1 + Ob2 
print(Ob3) 


# Python program to overload 
# a comparison operators 

class A: 
	def __init__(self, a): 
		self.a = a 
	def __gt__(self, other): 
		if(self.a>other.a): 
			return True
		else: 
			return False
ob1 = A(2) 
ob2 = A(3) 
if(ob1>ob2): 
	print("ob1 is greater than ob2") 
else: 
	print("ob2 is greater than ob1") 


	# Python program to overload equality 
# and less than operators 

class A: 
	def __init__(self, a): 
		self.a = a 
	def __lt__(self, other): 
		if(self.a<other.a): 
			return "ob1 is lessthan ob2"
		else: 
			return "ob2 is less than ob1"
	def __eq__(self, other): 
		if(self.a == other.a): 
			return "Both are equal"
		else: 
			return "Not equal"
				
ob1 = A(2) 
ob2 = A(3) 
print(ob1 < ob2) 

ob3 = A(4) 
ob4 = A(4) 
print(ob1 == ob2) 
