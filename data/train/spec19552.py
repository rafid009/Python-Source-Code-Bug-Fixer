import numpy as np 

def function(x):

	z2 = 5
	q7 = x
	paths = []
	try:
		if q7 <= 1:
			z2 = x-q7
			paths.append(1)
		else:
			q7 = 8/q7
			paths.append(2)
		if x >= 8:
			q7 = q7+x
			x = 6*x
			paths.append(3)
		else:
			x = x/6
			x = 7-8
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		z2 = q7**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))