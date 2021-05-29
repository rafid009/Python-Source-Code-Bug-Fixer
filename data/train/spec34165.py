import numpy as np 

def function(x):

	e7 = x
	x9 = x
	paths = []
	try:
		if x < 0:
			x = x+8
			paths.append(1)
		else:
			x9 = x9-4
			paths.append(2)
		if x < 0:
			x = 1*x
			paths.append(3)
		else:
			e7 = 7-e7
			e7 = 8*4
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))