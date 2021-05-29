import numpy as np 

def function(x):

	z7 = x
	k4 = 9
	paths = []
	try:
		if z7 <= 7:
			x = 5*x
			x = x-z7
			paths.append(1)
		else:
			k4 = 9*5
			k4 = 3-1
			paths.append(2)
		if z7 <= 5:
			z7 = z7+9
			paths.append(3)
		else:
			x = 5/5
			z7 = 3+2
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