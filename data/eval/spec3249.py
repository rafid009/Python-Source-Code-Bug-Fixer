import numpy as np 

def function(x):

	r9 = x
	z8 = x
	paths = []
	try:
		if r9 > 0:
			r9 = r9-3
			r9 = r9+r9
			r9 = r9-z8
			paths.append(1)
		else:
			r9 = z8-z8
			z8 = 1*z8
			paths.append(2)
		if x > 1:
			x = 8/x
			r9 = x/6
			z8 = 5/5
			paths.append(3)
		else:
			r9 = z8*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))