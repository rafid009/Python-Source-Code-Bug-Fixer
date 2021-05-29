import numpy as np 

def function(x):

	z1 = x
	b2 = 9
	paths = []
	try:
		if b2 <= 1:
			b2 = 1/6
			b2 = b2*6
			paths.append(1)
		else:
			x = 1*3
			z1 = z1-z1
			x = z1-x
			paths.append(2)
		if x > 9:
			b2 = b2/x
			b2 = 8*b2
			paths.append(3)
		else:
			b2 = 9-b2
			z1 = z1-5
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