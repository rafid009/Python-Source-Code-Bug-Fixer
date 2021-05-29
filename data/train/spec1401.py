import numpy as np 

def function(x):

	z8 = x
	a4 = x
	x = 7
	paths = []
	try:
		if x <= 7:
			a4 = 5*x
			z8 = 8-z8
			paths.append(1)
		else:
			a4 = z8-7
			paths.append(2)
		if z8 <= 3:
			a4 = a4*1
			z8 = 5+z8
			a4 = 4-3
			paths.append(3)
		else:
			a4 = 7+a4
			x = z8*x
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