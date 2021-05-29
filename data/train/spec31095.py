import numpy as np 

def function(x):

	e6 = x
	z6 = 1
	paths = []
	try:
		if e6 > 0:
			x = z6/x
			paths.append(1)
		else:
			e6 = 1-z6
			paths.append(2)
		if x < 3:
			x = x-3
			paths.append(3)
		else:
			x = x*z6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))