import numpy as np 

def function(x):

	v1 = x
	z5 = 7
	paths = []
	try:
		if x > 3:
			x = x*1
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if v1 <= 3:
			z5 = z5*z5
			paths.append(3)
		else:
			v1 = 6+v1
			z5 = z5*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))