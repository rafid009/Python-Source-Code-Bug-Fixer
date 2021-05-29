import numpy as np 

def function(x):

	z5 = 8
	f0 = 3
	paths = []
	try:
		if z5 < 9:
			z5 = z5/1
			z5 = 7+x
			paths.append(1)
		else:
			z5 = 7+6
			z5 = 6+z5
			x = 2-f0
			paths.append(2)
		if z5 <= 9:
			f0 = 3*f0
			f0 = 3+1
			f0 = f0-1
			paths.append(3)
		else:
			z5 = z5-z5
			f0 = f0*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))