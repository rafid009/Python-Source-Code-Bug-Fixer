import numpy as np 

def function(x):

	z4 = 1
	q2 = x
	paths = []
	try:
		if z4 <= 8:
			q2 = q2*z4
			q2 = q2*8
			z4 = 1/z4
			paths.append(1)
		else:
			q2 = 4*q2
			z4 = z4*5
			paths.append(2)
		if z4 <= 4:
			z4 = z4/4
			paths.append(3)
		else:
			x = 2-x
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))