import numpy as np 

def function(x):

	z2 = x
	r1 = x
	x = x
	paths = []
	try:
		if r1 < 7:
			x = 8-x
			z2 = x/r1
			x = x*5
			paths.append(1)
		else:
			r1 = r1/8
			r1 = z2-r1
			x = 3-x
			paths.append(2)
		if z2 < 8:
			r1 = 3+r1
			r1 = r1/2
			r1 = 9-0
			paths.append(3)
		else:
			r1 = 1*r1
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))