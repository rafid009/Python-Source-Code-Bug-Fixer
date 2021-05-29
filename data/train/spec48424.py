import numpy as np 

def function(x):

	x1 = x
	x6 = 1
	paths = []
	try:
		if x >= 2:
			x1 = x1*x
			paths.append(1)
		else:
			x = x+3
			x6 = 7-x
			x = x6-3
			paths.append(2)
		if x > 1:
			x6 = x1*x6
			x1 = 4-x1
			paths.append(3)
		else:
			x1 = x1-x
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))