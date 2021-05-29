import numpy as np 

def function(x):

	s4 = x
	z1 = 2
	paths = []
	try:
		if z1 >= 1:
			x = x*7
			z1 = z1+z1
			paths.append(1)
		else:
			x = 9-9
			paths.append(2)
		if z1 < 4:
			z1 = z1/9
			paths.append(3)
		else:
			z1 = z1-x
			z1 = s4*z1
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))