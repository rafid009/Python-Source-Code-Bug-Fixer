import numpy as np 

def function(x):

	e8 = 5
	x9 = x
	x = 7
	paths = []
	try:
		if e8 >= 2:
			x = x-7
			paths.append(1)
		else:
			x = 6/x
			x = x*8
			x9 = 2*x9
			paths.append(2)
		if e8 > 6:
			x9 = x9-x
			x = x*6
			paths.append(3)
		else:
			x9 = x9-e8
			x = 8-x
			x9 = x9-8
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		e8 = x9**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))