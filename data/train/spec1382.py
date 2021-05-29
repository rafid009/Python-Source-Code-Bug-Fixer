import numpy as np 

def function(x):

	z0 = 7
	u9 = 1
	paths = []
	try:
		if z0 < 0:
			x = x/8
			z0 = 7+z0
			z0 = 3-8
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x > 5:
			u9 = 9/u9
			x = x*x
			paths.append(3)
		else:
			u9 = u9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))