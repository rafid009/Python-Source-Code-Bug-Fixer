import numpy as np 

def function(x):

	e8 = x
	x3 = x
	paths = []
	try:
		if x < 1:
			e8 = e8-7
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if x3 <= 9:
			e8 = e8*5
			paths.append(3)
		else:
			x3 = x3*x3
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