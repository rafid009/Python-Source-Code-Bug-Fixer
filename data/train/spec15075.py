import numpy as np 

def function(x):

	x3 = x
	e7 = 1
	paths = []
	try:
		if e7 >= 6:
			x3 = 6+e7
			x3 = x3/x
			e7 = 4*e7
			paths.append(1)
		else:
			e7 = 7-e7
			paths.append(2)
		if x > 3:
			x = x-3
			e7 = e7*5
			paths.append(3)
		else:
			x3 = 0/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))