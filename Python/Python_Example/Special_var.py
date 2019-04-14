# File1.py 

	print "File1 __name__ = %s" %__name__ 

	if __name__ == "__main__": 
		print "File1 is being run directly"
	else: 
		print "File1 is being imported"


		# File2.py 

	import File1 

	print "File2 __name__ = %s" %__name__ 

	if __name__ == "__main__": 
		print "File2 is being run directly"
	else: 
		print "File2 is being imported"


	Now the interpreter is given the command to run File1.py.
	python File1.py
	Output :
	File1 __name__ = __main__
	File1 is being run directly


	And then File2.py is run.
	python File2.py
	Output :
	File1 __name__ = File1
	File1 is being imported
	File2 __name__ = __main__
	File2 is being run directly