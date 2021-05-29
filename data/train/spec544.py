import numpy as np 

def function(x):

	u1 = x
	z0 = 6
	paths = []
	try:
		if z0 < 0:
			x = x/2
			paths.append(1)
		else:
			z0 = z0+2
			z0 = z0*0
			paths.append(2)
		if x > 4:
			u1 = z0*4
			u1 = u1*8
			paths.append(3)
		else:
			u1 = u1-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))