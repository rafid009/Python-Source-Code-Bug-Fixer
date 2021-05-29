import numpy as np 

def function(x):

	e7 = x
	x7 = 6
	x = 5
	paths = []
	try:
		if e7 >= 2:
			x = x/3
			paths.append(1)
		else:
			x7 = 5*x7
			x7 = x7*1
			x = x-e7
			paths.append(2)
		if e7 >= 8:
			x7 = 3-x7
			x = x*6
			x7 = x7-1
			paths.append(3)
		else:
			x7 = 2*x7
			x7 = x7/x
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))