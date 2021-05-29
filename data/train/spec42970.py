import numpy as np 

def function(x):

	r6 = x
	z1 = x
	paths = []
	try:
		if z1 >= 6:
			z1 = z1+z1
			paths.append(1)
		else:
			x = x-r6
			z1 = 1+z1
			z1 = z1/1
			paths.append(2)
		if z1 > 6:
			z1 = 9*z1
			r6 = x-8
			paths.append(3)
		else:
			x = 9*z1
			r6 = r6-9
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))