import numpy as np 

def function(x):

	v9 = x
	z1 = x
	paths = []
	try:
		if x > 2:
			v9 = x/9
			v9 = v9-2
			paths.append(1)
		else:
			z1 = v9-z1
			paths.append(2)
		if x > 6:
			x = x-2
			paths.append(3)
		else:
			v9 = v9*8
			v9 = 1/v9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))