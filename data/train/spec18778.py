import numpy as np 

def function(x):

	z8 = x
	q9 = 3
	paths = []
	try:
		if q9 < 6:
			q9 = 0*q9
			paths.append(1)
		else:
			q9 = q9-4
			x = x/z8
			q9 = 7-1
			paths.append(2)
		if x <= 2:
			x = x-2
			q9 = z8*q9
			x = 5-q9
			paths.append(3)
		else:
			z8 = 3-x
			z8 = z8/3
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		q9 = z8**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))