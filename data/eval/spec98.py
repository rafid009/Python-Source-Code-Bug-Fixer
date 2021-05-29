import numpy as np 

def function(x):

	e6 = x
	y7 = 9
	x = 5
	paths = []
	try:
		if y7 <= 6:
			y7 = 8/y7
			paths.append(1)
		else:
			e6 = 0-e6
			paths.append(2)
		if x >= 0:
			y7 = 5*y7
			paths.append(3)
		else:
			y7 = y7-2
			e6 = e6*e6
			y7 = y7/8
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		y7 = e6**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))