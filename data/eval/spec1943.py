import numpy as np 

def function(x):

	z1 = 6
	d4 = 4
	paths = []
	try:
		if d4 >= 9:
			d4 = z1+d4
			z1 = 1-z1
			paths.append(1)
		else:
			z1 = 3+d4
			d4 = 2+d4
			d4 = 1+d4
			paths.append(2)
		if x >= 1:
			x = x+0
			z1 = 2-5
			paths.append(3)
		else:
			z1 = 1+2
			x = z1*d4
			z1 = d4+8
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))