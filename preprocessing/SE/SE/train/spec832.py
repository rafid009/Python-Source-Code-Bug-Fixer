import numpy as np 

def function(x):

	o5 = x
	z6 = 8
	paths = []
	try:
		if o5 <= 9:
			z6 = 5-4
			paths.append(1)
		else:
			o5 = 5+o5
			paths.append(2)
		if z6 < 6:
			x = o5*x
			paths.append(3)
		else:
			z6 = x+z6
			x = 4+z6
			x = x/z6
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		z6 = o5**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))