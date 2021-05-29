import numpy as np 

def function(x):

	q7 = 8
	z2 = 7
	paths = []
	try:
		if q7 <= 0:
			z2 = z2*1
			x = 3-x
			paths.append(1)
		else:
			q7 = q7+6
			paths.append(2)
		if z2 <= 3:
			z2 = q7/z2
			z2 = z2-0
			paths.append(3)
		else:
			z2 = z2+x
			q7 = q7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))