import numpy as np 

def function(x):

	z1 = 7
	x0 = x
	paths = []
	try:
		if x0 >= 9:
			x = 5-9
			paths.append(1)
		else:
			z1 = 8/z1
			paths.append(2)
		if x >= 1:
			z1 = z1*6
			x = x*x
			paths.append(3)
		else:
			x0 = 5*2
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