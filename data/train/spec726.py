import numpy as np 

def function(x):

	i0 = 1
	z7 = x
	paths = []
	try:
		if x >= 7:
			i0 = 0-x
			z7 = 2+z7
			paths.append(1)
		else:
			i0 = 1/i0
			paths.append(2)
		if z7 < 9:
			x = x*1
			paths.append(3)
		else:
			x = x/6
			i0 = i0*7
			i0 = i0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))