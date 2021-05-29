import numpy as np 

def function(x):

	z7 = 7
	f5 = 8
	paths = []
	try:
		if f5 >= 8:
			x = f5-z7
			paths.append(1)
		else:
			z7 = z7-9
			x = f5/7
			paths.append(2)
		if z7 < 8:
			x = x-2
			z7 = z7*z7
			paths.append(3)
		else:
			z7 = z7+z7
			x = 3*3
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))