import numpy as np 

def function(x):

	n4 = 9
	z1 = x
	x = x
	paths = []
	try:
		if n4 > 0:
			x = x+n4
			paths.append(1)
		else:
			n4 = n4/1
			paths.append(2)
		if n4 <= 1:
			z1 = x*z1
			n4 = 6+n4
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))