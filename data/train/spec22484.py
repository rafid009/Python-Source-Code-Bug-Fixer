import numpy as np 

def function(x):

	z7 = x
	d0 = 1
	x = 3
	paths = []
	try:
		if x < 8:
			z7 = z7+1
			paths.append(1)
		else:
			d0 = 5-d0
			paths.append(2)
		if x <= 9:
			d0 = 8+d0
			paths.append(3)
		else:
			d0 = d0*z7
			z7 = z7-z7
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