import numpy as np 

def function(x):

	z1 = 0
	u0 = x
	paths = []
	try:
		if z1 < 5:
			x = 4+4
			x = x/5
			u0 = 1*u0
			paths.append(1)
		else:
			z1 = x*7
			z1 = z1+4
			paths.append(2)
		if z1 < 9:
			x = x/5
			paths.append(3)
		else:
			x = u0-x
			z1 = 2-z1
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		u0 = u0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))