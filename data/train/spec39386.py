import numpy as np 

def function(x):

	d1 = 8
	z4 = 9
	paths = []
	try:
		if x < 1:
			d1 = 5/d1
			paths.append(1)
		else:
			x = 7-d1
			x = 5*x
			x = d1*6
			paths.append(2)
		if d1 <= 3:
			d1 = d1/z4
			z4 = z4*x
			d1 = 3*d1
			paths.append(3)
		else:
			z4 = z4*z4
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))