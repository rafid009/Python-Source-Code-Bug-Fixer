import numpy as np 

def function(x):

	x4 = 1
	a6 = x
	paths = []
	try:
		if x < 8:
			a6 = 0-4
			x = 6-x
			paths.append(1)
		else:
			a6 = a6*5
			a6 = a6+5
			paths.append(2)
		if x <= 2:
			x4 = x+a6
			x = 1-2
			paths.append(3)
		else:
			a6 = 3+x4
			x4 = x-x4
			a6 = x4*a6
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