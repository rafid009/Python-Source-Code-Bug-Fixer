import numpy as np 

def function(x):

	a4 = x
	z1 = x
	x = 8
	paths = []
	try:
		if z1 < 1:
			x = x/9
			paths.append(1)
		else:
			z1 = 2*a4
			x = x*4
			a4 = a4*a4
			paths.append(2)
		if x >= 9:
			z1 = 6-z1
			x = 5+z1
			z1 = x+z1
			paths.append(3)
		else:
			x = 8/x
			a4 = 1-x
			z1 = x*8
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))