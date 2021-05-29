import numpy as np 

def function(x):

	z0 = 0
	b2 = 1
	paths = []
	try:
		if z0 <= 2:
			x = x/1
			paths.append(1)
		else:
			b2 = b2*4
			paths.append(2)
		if x <= 5:
			z0 = 9/x
			paths.append(3)
		else:
			b2 = b2*3
			b2 = z0/x
			b2 = b2/x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))