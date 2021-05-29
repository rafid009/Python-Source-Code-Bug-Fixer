import numpy as np 

def function(x):

	x1 = 2
	v9 = 3
	paths = []
	try:
		if x < 6:
			v9 = 6+v9
			x1 = x1-x1
			paths.append(1)
		else:
			v9 = x/v9
			x1 = x1-x
			v9 = 1*v9
			paths.append(2)
		if x < 7:
			v9 = x+v9
			paths.append(3)
		else:
			v9 = v9-1
			x1 = 8-x
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