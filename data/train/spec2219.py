import numpy as np 

def function(x):

	q2 = 1
	z1 = x
	paths = []
	try:
		if q2 >= 0:
			z1 = z1+q2
			q2 = q2-7
			z1 = 5-3
			paths.append(1)
		else:
			z1 = 6/z1
			x = x/1
			paths.append(2)
		if x > 8:
			z1 = z1+8
			z1 = 7-0
			z1 = z1/1
			paths.append(3)
		else:
			x = 6*7
			x = q2+1
			q2 = 3/q2
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