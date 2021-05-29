import numpy as np 

def function(x):

	o4 = x
	z9 = 1
	paths = []
	try:
		if o4 < 0:
			z9 = z9/z9
			z9 = x+9
			paths.append(1)
		else:
			z9 = 1-6
			paths.append(2)
		if z9 > 6:
			o4 = o4*1
			paths.append(3)
		else:
			o4 = 6*o4
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))