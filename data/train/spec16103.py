import numpy as np 

def function(x):

	z5 = 8
	e7 = 1
	paths = []
	try:
		if z5 < 5:
			x = x*6
			x = 2+z5
			e7 = 2/e7
			paths.append(1)
		else:
			x = z5-0
			x = e7-8
			paths.append(2)
		if x <= 7:
			z5 = e7*2
			e7 = 4*5
			x = x+3
			paths.append(3)
		else:
			z5 = 0-z5
			x = 0/e7
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