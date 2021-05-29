import numpy as np 

def function(x):

	z1 = 2
	o0 = 6
	paths = []
	try:
		if x <= 7:
			x = 3-x
			o0 = 9-1
			paths.append(1)
		else:
			o0 = 5/o0
			o0 = o0+x
			paths.append(2)
		if x > 1:
			z1 = z1/o0
			z1 = 2-0
			o0 = 5/o0
			paths.append(3)
		else:
			z1 = 6+z1
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