import numpy as np 

def function(x):

	z7 = 3
	d0 = 5
	paths = []
	try:
		if z7 <= 2:
			d0 = d0-x
			paths.append(1)
		else:
			d0 = d0-z7
			d0 = d0/d0
			paths.append(2)
		if x < 4:
			z7 = 2/x
			x = z7+d0
			paths.append(3)
		else:
			d0 = 1-0
			z7 = x*d0
			d0 = d0+3
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