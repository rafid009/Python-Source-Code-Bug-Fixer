import numpy as np 

def function(x):

	u2 = 8
	e6 = 0
	paths = []
	try:
		if x >= 7:
			x = 3/8
			u2 = x-u2
			paths.append(1)
		else:
			u2 = u2*u2
			paths.append(2)
		if x >= 5:
			e6 = 4+6
			e6 = 4-e6
			paths.append(3)
		else:
			x = 2/8
			x = x-u2
			e6 = 5+7
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