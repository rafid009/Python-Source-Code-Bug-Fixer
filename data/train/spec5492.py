import numpy as np 

def function(x):

	e1 = x
	x1 = 9
	paths = []
	try:
		if x1 <= 1:
			x1 = 7-1
			x = x-e1
			paths.append(1)
		else:
			x1 = 0/2
			paths.append(2)
		if x1 >= 3:
			e1 = 2*e1
			e1 = x1*8
			paths.append(3)
		else:
			x1 = 0-x1
			e1 = x-x
			e1 = 8/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))