import numpy as np 

def function(x):

	z8 = 7
	y7 = x
	paths = []
	try:
		if z8 < 1:
			x = z8-y7
			paths.append(1)
		else:
			y7 = y7/6
			z8 = 4-z8
			paths.append(2)
		if x < 2:
			x = 3/x
			x = 0+1
			x = 1/x
			paths.append(3)
		else:
			x = 0+x
			x = x+6
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		x = z8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))