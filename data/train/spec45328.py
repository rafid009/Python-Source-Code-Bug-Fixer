import numpy as np 

def function(x):

	z1 = 6
	q1 = x
	paths = []
	try:
		if q1 > 9:
			q1 = 8*q1
			z1 = q1/9
			z1 = 0/z1
			paths.append(1)
		else:
			z1 = 5*8
			paths.append(2)
		if z1 >= 3:
			q1 = 3/q1
			z1 = 8-z1
			z1 = z1/z1
			paths.append(3)
		else:
			q1 = q1/6
			z1 = z1*1
			x = x*q1
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		z1 = q1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))