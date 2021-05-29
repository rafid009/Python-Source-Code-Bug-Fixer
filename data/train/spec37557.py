import numpy as np 

def function(x):

	x3 = x
	z7 = x
	paths = []
	try:
		if z7 >= 7:
			x3 = 1*x3
			paths.append(1)
		else:
			x3 = x3/2
			z7 = z7/3
			x3 = x3*1
			paths.append(2)
		if x3 <= 0:
			z7 = z7*z7
			x = x+z7
			paths.append(3)
		else:
			z7 = z7*x
			x3 = x3+x
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