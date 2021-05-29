import numpy as np 

def function(x):

	a8 = 1
	x1 = x
	paths = []
	try:
		if x1 <= 9:
			a8 = a8*x1
			a8 = 0-4
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if a8 < 9:
			a8 = a8*a8
			paths.append(3)
		else:
			x = 6*x1
			x = x*x
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