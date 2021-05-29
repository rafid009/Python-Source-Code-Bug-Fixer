import numpy as np 

def function(x):

	q1 = x
	z0 = x
	paths = []
	try:
		if q1 < 4:
			x = z0-9
			q1 = q1+z0
			paths.append(1)
		else:
			z0 = z0+3
			x = 4*5
			x = 0*x
			paths.append(2)
		if z0 < 3:
			q1 = q1+4
			q1 = 1-q1
			q1 = z0/q1
			paths.append(3)
		else:
			q1 = 1*0
			z0 = 1/z0
			q1 = q1*x
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))