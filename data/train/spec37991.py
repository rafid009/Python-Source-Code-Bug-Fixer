import numpy as np 

def function(x):

	o8 = 2
	z8 = x
	paths = []
	try:
		if o8 > 6:
			x = 9/o8
			paths.append(1)
		else:
			z8 = z8+4
			paths.append(2)
		if z8 < 8:
			o8 = o8*z8
			z8 = 4-o8
			paths.append(3)
		else:
			o8 = o8/5
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))