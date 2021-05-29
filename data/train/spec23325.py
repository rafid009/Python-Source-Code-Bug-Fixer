import numpy as np 

def function(x):

	z7 = x
	y6 = x
	paths = []
	try:
		if y6 < 0:
			y6 = y6-7
			x = 3+8
			x = 3/x
			paths.append(1)
		else:
			z7 = z7-y6
			x = 5-x
			x = x+6
			paths.append(2)
		if y6 >= 6:
			y6 = y6+9
			paths.append(3)
		else:
			x = x-4
			z7 = 2*y6
			z7 = 5*x
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))