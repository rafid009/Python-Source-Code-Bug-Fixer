import numpy as np 

def function(x):

	v1 = x
	z0 = 8
	paths = []
	try:
		if z0 > 5:
			x = 9/v1
			paths.append(1)
		else:
			x = 9-x
			v1 = 1/v1
			paths.append(2)
		if z0 <= 9:
			z0 = v1+7
			paths.append(3)
		else:
			v1 = 5*3
			z0 = x-z0
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		z0 = v1**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))