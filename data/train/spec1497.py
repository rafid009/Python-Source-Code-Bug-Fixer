import numpy as np 

def function(x):

	z0 = x
	d5 = 7
	paths = []
	try:
		if x >= 6:
			x = z0+x
			z0 = x*d5
			d5 = d5+d5
			paths.append(1)
		else:
			d5 = 3+d5
			paths.append(2)
		if d5 > 9:
			d5 = d5/9
			d5 = d5+5
			paths.append(3)
		else:
			d5 = d5-5
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))