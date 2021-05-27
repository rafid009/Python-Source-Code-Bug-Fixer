import numpy as np 

def function(x):

	z8 = 9
	i7 = x
	paths = []
	try:
		if z8 >= 4:
			i7 = 7+3
			i7 = i7-1
			x = x-0
			paths.append(1)
		else:
			z8 = 8+z8
			i7 = i7-x
			i7 = 8/i7
			paths.append(2)
		if z8 < 7:
			i7 = i7/i7
			z8 = x*z8
			x = x*8
			paths.append(3)
		else:
			z8 = 6+z8
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