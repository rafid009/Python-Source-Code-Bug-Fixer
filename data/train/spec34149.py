import numpy as np 

def function(x):

	x7 = x
	v1 = 3
	paths = []
	try:
		if v1 >= 2:
			x = 6*x
			x7 = x7-7
			paths.append(1)
		else:
			x = 0-7
			v1 = x7/x7
			paths.append(2)
		if v1 > 5:
			x = x-6
			x = x+5
			x = x/x7
			paths.append(3)
		else:
			x7 = x-x7
			v1 = 6/v1
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))