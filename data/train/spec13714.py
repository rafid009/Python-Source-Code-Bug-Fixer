import numpy as np 

def function(x):

	y7 = 7
	x5 = x
	paths = []
	try:
		if x5 >= 4:
			y7 = y7*x
			paths.append(1)
		else:
			x = 9-4
			x = 8/x
			y7 = 9/y7
			paths.append(2)
		if x5 >= 3:
			x5 = 0+y7
			y7 = y7-8
			paths.append(3)
		else:
			x = 7/x
			x5 = y7*x
			x = x-9
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