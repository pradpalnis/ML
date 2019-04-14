# Ignore a value of specific location/index 
for _ in range(10) :
	print ("Test")
 
class MyClass(): 
	 def __init__(self): 
			 print ("OWK")

def my_defination(var1 = 1, class_ = MyClass): 
	 print (var1 )
	 print (class_)

my_defination() 

class Prefix: 
	 def __init__(self): 
			 self.public = 10
			 self._private = 12
test = Prefix() 
print(test.public )

print (test._private )


#Python class_file.py
def public_api(): 
    print ("public api")
    
def _private_api(): 
    print ("private api"    )
    
from class_file import *
public_api() 

  
_private_api() 

import class_file 
class_file.public_api() 

class_file._private_api() 



 
#testFile.py
class Myclass(): 
	def __init__(self): 
		self.__variable = 10

  #Calling from Interpreter
>>> import testFile 
>>> obj = testFile.Myclass() 
>>> obj.__variable 
Traceback (most recent call last): 
File "", line 1, in
AttributeError: Myclass instance has no attribute '__variable'
nce has no attribute 'Myclass'
>>> obj._Myclass__variable 
10

class Myclass(): 
	def __init__(self): 
		self.__variable = 10
	def func(self) 
		print self.__variable 

  
>>> import testFile 
>>> obj = testFile.Myclass() 
>>> obj.func() 
10


class Myclass(): 
	def __add__(self,a,b): 
		print a*b 


>>> import testFile 
>>> obj = testFile.Myclass() 
>>> obj.__add__(1,2) 
2
>>> obj.__add__(5,2) 
10
  