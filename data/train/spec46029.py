import numpy as np 

def function(x):

	b6 = 3
	z8 = 3
	paths = []
	try:
		if b6 <= 2:
			x = x/6
			paths.append(1)
		else:
			z8 = z8/z8
			paths.append(2)
		if b6 > 6:
			b6 = b6*4
			paths.append(3)
		else:
			x = x*6
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