import numpy as np 

def function(x):

	u9 = 4
	z8 = 3
	paths = []
	try:
		if z8 > 8:
			z8 = 8/5
			x = 9-u9
			paths.append(1)
		else:
			u9 = z8/5
			paths.append(2)
		if z8 < 6:
			z8 = z8/8
			x = 1-x
			u9 = 2-6
			paths.append(3)
		else:
			u9 = u9*5
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))