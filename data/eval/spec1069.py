import numpy as np 

def function(x):

	q0 = x
	z6 = 5
	paths = []
	try:
		if q0 <= 7:
			q0 = 2*q0
			paths.append(1)
		else:
			x = x+x
			x = q0*x
			paths.append(2)
		if x > 1:
			x = x+q0
			q0 = z6*x
			paths.append(3)
		else:
			z6 = z6/x
			x = 6/8
			q0 = 6-x
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))