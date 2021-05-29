import numpy as np 

def function(x):

	j0 = 5
	x1 = 8
	paths = []
	try:
		if x > 0:
			x = x+6
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if x >= 9:
			x1 = x1*j0
			paths.append(3)
		else:
			j0 = 3-j0
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