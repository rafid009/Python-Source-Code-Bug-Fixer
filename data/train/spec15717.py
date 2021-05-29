import numpy as np 

def function(x):

	y7 = x
	y5 = 5
	paths = []
	try:
		if y5 <= 9:
			x = y7-2
			paths.append(1)
		else:
			y7 = 9/x
			paths.append(2)
		if x >= 5:
			x = x-y7
			x = 6/6
			x = 4/y7
			paths.append(3)
		else:
			y5 = 9-5
			y7 = y7/y7
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