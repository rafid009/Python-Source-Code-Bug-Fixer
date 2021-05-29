import numpy as np 

def function(x):

	e4 = 2
	l8 = 6
	x = x
	paths = []
	try:
		if l8 >= 6:
			e4 = 0+e4
			e4 = 3*6
			paths.append(1)
		else:
			l8 = 8*l8
			paths.append(2)
		if l8 >= 2:
			e4 = e4/3
			e4 = e4/l8
			x = 3/x
			paths.append(3)
		else:
			x = x+l8
			l8 = 6-e4
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