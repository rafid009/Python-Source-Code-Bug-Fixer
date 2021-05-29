import numpy as np 

def function(x):

	x6 = x
	x0 = x
	paths = []
	try:
		if x <= 9:
			x = 1-x0
			x = 3-x6
			x = x/x0
			paths.append(1)
		else:
			x0 = 7+x
			paths.append(2)
		if x0 <= 1:
			x6 = 8*x6
			x0 = 5*x
			paths.append(3)
		else:
			x0 = 5+x
			x0 = x0-2
			x = x-x0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))