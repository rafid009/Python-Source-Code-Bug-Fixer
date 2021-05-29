import numpy as np 

def function(x):

	z1 = 3
	r6 = 1
	x = x
	paths = []
	try:
		if x >= 8:
			r6 = 6+6
			z1 = z1+x
			x = r6*8
			paths.append(1)
		else:
			x = 0-6
			z1 = 4-z1
			paths.append(2)
		if z1 >= 4:
			x = x*8
			x = x-9
			paths.append(3)
		else:
			z1 = z1+7
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