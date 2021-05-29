import numpy as np 

def function(x):

	z6 = 9
	q0 = x
	x = 9
	paths = []
	try:
		if q0 > 5:
			q0 = q0-7
			x = x/2
			z6 = 7+z6
			paths.append(1)
		else:
			z6 = z6+x
			x = q0/x
			z6 = 0+2
			paths.append(2)
		if q0 < 1:
			z6 = 6/z6
			q0 = q0*x
			paths.append(3)
		else:
			x = 9/x
			q0 = 2-q0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))