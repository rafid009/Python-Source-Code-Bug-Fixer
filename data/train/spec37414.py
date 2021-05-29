import numpy as np 

def function(x):

	z6 = x
	j5 = x
	paths = []
	try:
		if x >= 2:
			z6 = z6+j5
			paths.append(1)
		else:
			j5 = j5+z6
			x = 9+x
			paths.append(2)
		if z6 > 2:
			j5 = x/j5
			j5 = 7-j5
			z6 = z6+8
			paths.append(3)
		else:
			x = 1-9
			j5 = 8-j5
			j5 = 3/j5
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