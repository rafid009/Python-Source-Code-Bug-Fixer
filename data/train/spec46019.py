import numpy as np 

def function(x):

	y7 = 4
	a3 = 2
	paths = []
	try:
		if a3 <= 0:
			x = y7*3
			a3 = 5*y7
			a3 = a3*6
			paths.append(1)
		else:
			x = 0-3
			a3 = a3/6
			a3 = 8-9
			paths.append(2)
		if x <= 4:
			a3 = y7+y7
			paths.append(3)
		else:
			y7 = 3/y7
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