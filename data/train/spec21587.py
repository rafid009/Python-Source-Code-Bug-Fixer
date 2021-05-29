import numpy as np 

def function(x):

	e6 = x
	y7 = 0
	paths = []
	try:
		if y7 >= 0:
			y7 = e6-0
			y7 = 8*y7
			y7 = e6+e6
			paths.append(1)
		else:
			y7 = 8/4
			y7 = y7+y7
			paths.append(2)
		if y7 >= 2:
			y7 = 7+y7
			y7 = e6*y7
			paths.append(3)
		else:
			y7 = 0-e6
			e6 = y7/5
			e6 = 9/8
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