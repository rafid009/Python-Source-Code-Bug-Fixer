import numpy as np 

def function(x):

	k7 = x
	y1 = x
	paths = []
	try:
		if x >= 8:
			x = 6/y1
			paths.append(1)
		else:
			x = x*y1
			paths.append(2)
		if x < 1:
			y1 = 1-9
			k7 = k7/x
			paths.append(3)
		else:
			y1 = y1-9
			x = 2+7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))