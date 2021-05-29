import numpy as np 

def function(x):

	z8 = 1
	r5 = 8
	x = x
	paths = []
	try:
		if x > 1:
			x = x-0
			paths.append(1)
		else:
			z8 = x+z8
			x = x/1
			z8 = 2/r5
			paths.append(2)
		if z8 > 8:
			r5 = z8*6
			x = 4*9
			paths.append(3)
		else:
			z8 = z8-6
			r5 = r5+0
			r5 = r5/z8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))