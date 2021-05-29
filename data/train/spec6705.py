import numpy as np 

def function(x):

	z8 = x
	o0 = x
	paths = []
	try:
		if z8 >= 5:
			o0 = 3+o0
			x = 9*x
			paths.append(1)
		else:
			o0 = o0/9
			o0 = o0*z8
			paths.append(2)
		if z8 >= 6:
			z8 = 5*5
			paths.append(3)
		else:
			z8 = 1/z8
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		o0 = z8**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))