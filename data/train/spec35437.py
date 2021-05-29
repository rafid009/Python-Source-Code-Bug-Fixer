import numpy as np 

def function(x):

	q7 = 5
	z6 = 1
	paths = []
	try:
		if x < 7:
			q7 = q7*q7
			paths.append(1)
		else:
			z6 = z6+q7
			paths.append(2)
		if x < 3:
			z6 = x-6
			z6 = 4-z6
			x = q7+0
			paths.append(3)
		else:
			z6 = 9+q7
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))