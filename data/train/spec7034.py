import numpy as np 

def function(x):

	v4 = x
	z4 = 1
	paths = []
	try:
		if z4 <= 9:
			z4 = x/v4
			z4 = 2*v4
			paths.append(1)
		else:
			x = z4-7
			v4 = 2-0
			paths.append(2)
		if v4 <= 7:
			v4 = x+x
			paths.append(3)
		else:
			z4 = 5*8
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