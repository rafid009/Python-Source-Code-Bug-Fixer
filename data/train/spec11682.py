import numpy as np 

def function(x):

	e3 = x
	z8 = x
	paths = []
	try:
		if x <= 3:
			e3 = 6+e3
			e3 = 8+e3
			x = x/4
			paths.append(1)
		else:
			x = x/6
			z8 = 9-7
			z8 = z8+6
			paths.append(2)
		if e3 >= 1:
			e3 = e3+z8
			x = 4/x
			x = 5/x
			paths.append(3)
		else:
			x = x-5
			x = 8-z8
			z8 = z8*9
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z8 = z8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))