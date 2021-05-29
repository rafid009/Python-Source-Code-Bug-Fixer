import numpy as np 

def function(x):

	q1 = x
	z1 = 6
	paths = []
	try:
		if z1 >= 9:
			x = x-z1
			z1 = z1+9
			paths.append(1)
		else:
			z1 = z1/2
			q1 = q1+7
			paths.append(2)
		if z1 > 5:
			z1 = 3*z1
			x = 0-8
			paths.append(3)
		else:
			x = x/q1
			x = x-2
			z1 = z1+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))