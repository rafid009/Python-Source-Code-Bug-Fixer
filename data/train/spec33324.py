import numpy as np 

def function(x):

	z8 = 2
	a2 = x
	paths = []
	try:
		if x <= 3:
			z8 = z8-8
			z8 = 3/z8
			z8 = 6/z8
			paths.append(1)
		else:
			a2 = a2-5
			a2 = 5/1
			paths.append(2)
		if z8 >= 8:
			x = z8*5
			paths.append(3)
		else:
			x = x-a2
			x = x-4
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		x = z8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))