import numpy as np 

def function(x):

	z7 = x
	r1 = 9
	paths = []
	try:
		if x <= 2:
			z7 = z7-6
			x = x+4
			paths.append(1)
		else:
			z7 = 7+z7
			paths.append(2)
		if z7 > 1:
			x = r1/7
			paths.append(3)
		else:
			z7 = 0+z7
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