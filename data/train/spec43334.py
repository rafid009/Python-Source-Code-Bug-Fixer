import numpy as np 

def function(x):

	o0 = x
	z5 = 2
	x = 6
	paths = []
	try:
		if z5 >= 2:
			o0 = 4/o0
			z5 = 7-4
			x = x*x
			paths.append(1)
		else:
			x = x-8
			x = 3-x
			paths.append(2)
		if o0 >= 3:
			z5 = o0+2
			z5 = z5/3
			paths.append(3)
		else:
			o0 = o0-1
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		x = o0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))