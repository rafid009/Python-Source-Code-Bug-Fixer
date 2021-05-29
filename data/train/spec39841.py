import numpy as np 

def function(x):

	b1 = 6
	z0 = 8
	paths = []
	try:
		if z0 < 1:
			x = x*3
			paths.append(1)
		else:
			z0 = x-0
			b1 = b1-x
			b1 = x+7
			paths.append(2)
		if z0 >= 7:
			z0 = 9*z0
			z0 = z0/x
			x = x*2
			paths.append(3)
		else:
			x = b1*z0
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		z0 = b1**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))