import numpy as np 

def function(x):

	z1 = x
	x1 = x
	paths = []
	try:
		if x < 2:
			z1 = 6-z1
			x = 7+x
			paths.append(1)
		else:
			x = x1+4
			x1 = x1-7
			paths.append(2)
		if z1 >= 4:
			x = x/8
			x1 = 2-x1
			paths.append(3)
		else:
			z1 = x-x1
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