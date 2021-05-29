import numpy as np 

def function(x):

	o7 = x
	z7 = x
	paths = []
	try:
		if z7 < 2:
			x = x-0
			z7 = z7+0
			paths.append(1)
		else:
			o7 = o7+7
			z7 = o7+z7
			x = x-x
			paths.append(2)
		if o7 >= 1:
			x = z7*o7
			o7 = 6/o7
			paths.append(3)
		else:
			x = x/z7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		z7 = z7**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))