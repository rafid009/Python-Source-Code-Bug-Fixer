import numpy as np 

def function(x):

	z8 = 5
	o4 = x
	paths = []
	try:
		if x > 7:
			o4 = x-o4
			x = x+4
			paths.append(1)
		else:
			z8 = z8*8
			paths.append(2)
		if x > 7:
			z8 = z8*4
			z8 = z8-x
			o4 = x-6
			paths.append(3)
		else:
			z8 = z8*4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))