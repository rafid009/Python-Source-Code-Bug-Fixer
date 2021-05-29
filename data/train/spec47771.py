import numpy as np 

def function(x):

	z1 = 6
	o7 = x
	paths = []
	try:
		if z1 <= 6:
			o7 = 6+o7
			z1 = 5/z1
			paths.append(1)
		else:
			z1 = z1+z1
			z1 = z1*5
			o7 = x*6
			paths.append(2)
		if o7 >= 1:
			x = z1*9
			paths.append(3)
		else:
			x = x-o7
			z1 = 8*3
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))