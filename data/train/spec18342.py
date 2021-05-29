import numpy as np 

def function(x):

	o5 = 1
	z9 = 1
	paths = []
	try:
		if z9 > 0:
			z9 = o5+3
			x = 3-x
			o5 = o5-4
			paths.append(1)
		else:
			x = 9/o5
			z9 = x*o5
			o5 = 5/x
			paths.append(2)
		if x <= 0:
			x = x-6
			paths.append(3)
		else:
			z9 = z9*7
			z9 = z9-1
			z9 = x+z9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))