import numpy as np 

def function(x):

	y8 = x
	x1 = 7
	paths = []
	try:
		if y8 >= 1:
			x1 = x1-2
			paths.append(1)
		else:
			x = y8+x
			x1 = 5+x1
			y8 = 1/6
			paths.append(2)
		if y8 >= 3:
			y8 = y8/x1
			paths.append(3)
		else:
			y8 = y8-5
			y8 = 3*y8
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		x = y8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))