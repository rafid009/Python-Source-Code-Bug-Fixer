import numpy as np 

def function(x):

	z0 = 3
	u6 = x
	paths = []
	try:
		if x >= 8:
			x = 4-u6
			paths.append(1)
		else:
			z0 = 8/z0
			x = 3+x
			z0 = z0+u6
			paths.append(2)
		if x > 3:
			u6 = u6-1
			z0 = 7+z0
			x = 3*x
			paths.append(3)
		else:
			z0 = z0*0
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