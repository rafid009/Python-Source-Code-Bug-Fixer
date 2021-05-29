import numpy as np 

def function(x):

	o5 = x
	z9 = 2
	paths = []
	try:
		if z9 < 9:
			o5 = o5*4
			o5 = o5/7
			paths.append(1)
		else:
			z9 = z9+1
			x = 1+1
			x = 3*x
			paths.append(2)
		if o5 < 3:
			o5 = o5-x
			o5 = o5-7
			z9 = 8-z9
			paths.append(3)
		else:
			x = 1+4
			o5 = 6+o5
			z9 = 6+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))