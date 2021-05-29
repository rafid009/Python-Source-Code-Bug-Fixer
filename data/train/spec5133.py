import numpy as np 

def function(x):

	i0 = x
	z6 = 8
	paths = []
	try:
		if z6 < 6:
			x = x*i0
			z6 = 4-6
			paths.append(1)
		else:
			i0 = i0-9
			paths.append(2)
		if x >= 1:
			z6 = z6/z6
			x = x-7
			i0 = z6/i0
			paths.append(3)
		else:
			i0 = x*x
			x = x/5
			x = 2/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))