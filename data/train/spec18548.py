import numpy as np 

def function(x):

	z8 = x
	r0 = x
	paths = []
	try:
		if x <= 0:
			x = z8-5
			paths.append(1)
		else:
			x = x/9
			z8 = 2*r0
			paths.append(2)
		if z8 >= 2:
			r0 = r0-z8
			z8 = z8+8
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))