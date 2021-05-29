import numpy as np 

def function(x):

	l9 = 9
	z4 = 3
	paths = []
	try:
		if x > 2:
			x = x+0
			paths.append(1)
		else:
			z4 = z4-0
			paths.append(2)
		if x > 5:
			x = x-l9
			x = x+l9
			z4 = 5+8
			paths.append(3)
		else:
			x = x/6
			z4 = 0+4
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))