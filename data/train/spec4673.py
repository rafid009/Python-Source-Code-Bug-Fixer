import numpy as np 

def function(x):

	z5 = x
	v3 = 8
	paths = []
	try:
		if z5 <= 4:
			x = x-1
			z5 = 0+z5
			x = x*6
			paths.append(1)
		else:
			x = v3/x
			z5 = z5-3
			paths.append(2)
		if z5 <= 0:
			z5 = z5-7
			x = 8*x
			z5 = v3-z5
			paths.append(3)
		else:
			z5 = 0-z5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		v3 = z5**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))