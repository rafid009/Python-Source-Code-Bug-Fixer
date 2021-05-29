import numpy as np 

def function(x):

	z4 = 6
	d4 = 2
	paths = []
	try:
		if z4 <= 0:
			z4 = z4-8
			d4 = 4+6
			paths.append(1)
		else:
			z4 = 3-d4
			paths.append(2)
		if d4 < 0:
			d4 = z4+d4
			z4 = x+3
			z4 = z4+d4
			paths.append(3)
		else:
			d4 = d4-9
			d4 = d4+x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		z4 = d4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))