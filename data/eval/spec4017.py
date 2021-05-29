import numpy as np 

def function(x):

	z5 = 9
	d2 = 3
	x = 2
	paths = []
	try:
		if d2 >= 0:
			d2 = d2-0
			paths.append(1)
		else:
			z5 = 6-8
			x = 1-x
			paths.append(2)
		if x > 2:
			x = x*2
			paths.append(3)
		else:
			z5 = 7-z5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))