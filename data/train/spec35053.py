import numpy as np 

def function(x):

	d9 = 9
	z9 = 3
	paths = []
	try:
		if z9 < 8:
			d9 = d9-9
			z9 = z9*d9
			z9 = z9+9
			paths.append(1)
		else:
			d9 = x-3
			x = 8/x
			paths.append(2)
		if x <= 6:
			z9 = d9*5
			x = 2-x
			paths.append(3)
		else:
			x = x-8
			d9 = 6/x
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		d9 = d9**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))