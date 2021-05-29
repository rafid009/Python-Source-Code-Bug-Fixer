import numpy as np 

def function(x):

	s7 = 2
	z1 = x
	paths = []
	try:
		if z1 >= 5:
			z1 = z1/1
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if z1 <= 7:
			x = z1-x
			paths.append(3)
		else:
			z1 = 5-z1
			s7 = 8+0
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