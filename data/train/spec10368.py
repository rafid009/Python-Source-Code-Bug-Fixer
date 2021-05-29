import numpy as np 

def function(x):

	f1 = 3
	d7 = x
	paths = []
	try:
		if x >= 6:
			f1 = 3*f1
			f1 = 0-f1
			paths.append(1)
		else:
			f1 = 6/7
			x = f1*d7
			x = 0-x
			paths.append(2)
		if x < 2:
			f1 = f1*3
			paths.append(3)
		else:
			x = x-f1
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