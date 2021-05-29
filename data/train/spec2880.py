import numpy as np 

def function(x):

	z6 = 4
	d5 = 3
	paths = []
	try:
		if d5 > 7:
			z6 = z6/2
			x = 8/x
			paths.append(1)
		else:
			d5 = d5/2
			d5 = 3+d5
			paths.append(2)
		if z6 >= 5:
			x = x*d5
			d5 = 9/2
			z6 = z6/9
			paths.append(3)
		else:
			d5 = 7+d5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))