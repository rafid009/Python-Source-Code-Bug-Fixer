import numpy as np 

def function(x):

	o9 = 7
	z5 = x
	paths = []
	try:
		if z5 > 2:
			o9 = 1-o9
			z5 = z5/4
			paths.append(1)
		else:
			z5 = z5-7
			o9 = o9*6
			paths.append(2)
		if x > 7:
			x = x-o9
			z5 = 5-0
			paths.append(3)
		else:
			o9 = 6/o9
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		z5 = o9**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))