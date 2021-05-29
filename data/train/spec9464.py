import numpy as np 

def function(x):

	z4 = 1
	e0 = 4
	paths = []
	try:
		if x > 8:
			z4 = 2*z4
			x = 5*6
			x = x*9
			paths.append(1)
		else:
			e0 = 2/7
			e0 = 1-e0
			paths.append(2)
		if z4 >= 0:
			x = e0+x
			paths.append(3)
		else:
			x = x+0
			e0 = 1-e0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))