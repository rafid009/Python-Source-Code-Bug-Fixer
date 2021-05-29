import numpy as np 

def function(x):

	i0 = x
	z7 = x
	paths = []
	try:
		if x > 8:
			i0 = 8/4
			x = x-8
			x = 6-0
			paths.append(1)
		else:
			i0 = 5+i0
			paths.append(2)
		if i0 < 2:
			i0 = i0/6
			z7 = 6*z7
			paths.append(3)
		else:
			i0 = 4+i0
			z7 = 5/3
			z7 = z7-9
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