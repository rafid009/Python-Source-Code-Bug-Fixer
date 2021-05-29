import numpy as np 

def function(x):

	z9 = 6
	o7 = 0
	paths = []
	try:
		if z9 <= 9:
			z9 = o7-z9
			o7 = x*z9
			paths.append(1)
		else:
			o7 = x-x
			o7 = 3+z9
			paths.append(2)
		if x >= 0:
			z9 = x/2
			paths.append(3)
		else:
			o7 = 4/o7
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