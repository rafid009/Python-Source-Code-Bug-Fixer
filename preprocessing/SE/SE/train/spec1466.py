import numpy as np 

def function(x):

	o6 = x
	z9 = 3
	paths = []
	try:
		if o6 < 6:
			z9 = 3/z9
			x = 7+x
			o6 = x+9
			paths.append(1)
		else:
			o6 = 8/o6
			z9 = 9/z9
			o6 = o6-9
			paths.append(2)
		if o6 < 4:
			z9 = z9*8
			paths.append(3)
		else:
			x = x-x
			x = 2*5
			o6 = z9+o6
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