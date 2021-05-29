import numpy as np 

def function(x):

	e3 = 9
	a4 = 8
	paths = []
	try:
		if x >= 1:
			x = 0-8
			paths.append(1)
		else:
			e3 = e3+4
			paths.append(2)
		if x >= 4:
			a4 = e3/3
			paths.append(3)
		else:
			x = x-8
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