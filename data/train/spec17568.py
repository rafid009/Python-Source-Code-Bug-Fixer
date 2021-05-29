import numpy as np 

def function(x):

	y7 = x
	y4 = 4
	x = 2
	paths = []
	try:
		if x > 8:
			y7 = 9*y7
			paths.append(1)
		else:
			x = 6*9
			y7 = 9-y7
			paths.append(2)
		if x >= 9:
			y4 = y4+2
			x = 1/x
			paths.append(3)
		else:
			y4 = y4*x
			x = 1+y4
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))