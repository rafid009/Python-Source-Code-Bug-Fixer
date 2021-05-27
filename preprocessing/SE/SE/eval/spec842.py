import numpy as np 

def function(x):

	e3 = 2
	z1 = x
	paths = []
	try:
		if e3 < 9:
			z1 = x-z1
			paths.append(1)
		else:
			e3 = 7*e3
			e3 = x-2
			z1 = z1-z1
			paths.append(2)
		if x < 7:
			e3 = 0-e3
			x = x+9
			paths.append(3)
		else:
			x = x*1
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