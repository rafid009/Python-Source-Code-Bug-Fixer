import numpy as np 

def function(x):

	y5 = x
	q8 = x
	paths = []
	try:
		if y5 > 6:
			q8 = 5*x
			y5 = y5*9
			paths.append(1)
		else:
			q8 = y5-4
			paths.append(2)
		if x >= 4:
			y5 = 6*y5
			paths.append(3)
		else:
			x = x+6
			q8 = 3-y5
			q8 = 9/q8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))