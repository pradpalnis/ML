# Python code to illustrate how mangling works 
class Map: 
	def __init__(self, iterate): 
		self.list = [] 
		self.__geek(iterate) 
	def geek(self, iterate): 
		for item in iterate: 
			self.list.append(item) 

	# private copy of original geek() method 
	__geek = geek 

class MapSubclass(Map): 
	
	# provides new signature for geek() but 
	# does not break __init__() 
	def geek(self, key, value):		 
		for i in zip(keys, values): 
			self.list.append(i) 
   
   
# Python code to illustrate 
# how single underscore works 
def _get_errors(self): 
	if self._errors is None: 
		self.full_clean() 
	return self._errors 

errors = property(_get_errors) 


# Python code to illustrate how double 
# underscore at the beginning works 
class Geek: 
	def _single_method(self): 
		pass
	def __double_method(self): # for mangling 
		pass
class Pyth(Geek): 
	def __double_method(self): # for mangling 
		pass


# Python code to illustrate double leading and 
# double trailing underscore works 
class Geek: 

	# '__init__' for initializing, this is a 
	# special method 
	def __init__(self, ab): 
		self.ab = ab 

	# custom special method. try not to use it 
	def __custom__(self): 
		pass
   
