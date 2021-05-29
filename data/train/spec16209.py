import numpy as np 

def function(x):

	x8 = x
	e4 = x
	x = 6
	paths = []
	try:
		if x8 >= 7:
			x = x-x
			x8 = 3*x8
			e4 = 5*e4
			paths.append(1)
		else:
			e4 = 5+e4
			x8 = 9*x8
			paths.append(2)
		if x >= 9:
			x = 5/x
			x = 5-x
			paths.append(3)
		else:
			x8 = 6/x8
			e4 = 8+x8
			x = 6*5
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		e4 = x8**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))