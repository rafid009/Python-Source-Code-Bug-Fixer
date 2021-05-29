import numpy as np 

def function(x):

	e0 = 2
	z1 = 3
	x = x
	paths = []
	try:
		if z1 < 6:
			e0 = e0/3
			z1 = e0/9
			paths.append(1)
		else:
			x = 8/z1
			x = x*0
			e0 = e0+z1
			paths.append(2)
		if x <= 7:
			z1 = z1+4
			z1 = z1-2
			paths.append(3)
		else:
			z1 = e0-x
			z1 = e0/z1
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