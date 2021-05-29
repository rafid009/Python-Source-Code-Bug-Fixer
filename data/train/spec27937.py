import numpy as np 

def function(x):

	z4 = 0
	u0 = x
	paths = []
	try:
		if z4 >= 4:
			u0 = x*u0
			paths.append(1)
		else:
			x = x+x
			x = x-2
			x = z4-x
			paths.append(2)
		if z4 > 3:
			z4 = 3+1
			paths.append(3)
		else:
			z4 = z4+8
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))