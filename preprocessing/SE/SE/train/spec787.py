import numpy as np 

def function(x):

	z1 = 4
	r1 = x
	paths = []
	try:
		if z1 >= 4:
			r1 = r1-4
			paths.append(1)
		else:
			r1 = 9*8
			r1 = z1+r1
			z1 = z1*8
			paths.append(2)
		if r1 >= 6:
			x = x/6
			r1 = x-r1
			paths.append(3)
		else:
			x = 9-x
			z1 = 6-5
			z1 = z1*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))