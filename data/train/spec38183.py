import numpy as np 

def function(x):

	z1 = 2
	u0 = x
	paths = []
	try:
		if z1 <= 5:
			u0 = 4+u0
			u0 = 3+2
			paths.append(1)
		else:
			u0 = u0+4
			z1 = 1*0
			z1 = z1/3
			paths.append(2)
		if x > 6:
			u0 = 8/u0
			paths.append(3)
		else:
			u0 = 7/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))