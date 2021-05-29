import numpy as np 

def function(x):

	z0 = 1
	v4 = x
	x = x
	paths = []
	try:
		if v4 <= 1:
			z0 = 7*x
			paths.append(1)
		else:
			z0 = 1*z0
			z0 = v4+z0
			paths.append(2)
		if z0 >= 5:
			z0 = 5-1
			paths.append(3)
		else:
			v4 = x+v4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))