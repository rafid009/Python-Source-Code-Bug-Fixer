import numpy as np 

def function(x):

	z8 = x
	q4 = 7
	paths = []
	try:
		if z8 > 6:
			q4 = q4*q4
			z8 = 0-q4
			x = z8-x
			paths.append(1)
		else:
			q4 = 6*q4
			paths.append(2)
		if x < 3:
			q4 = q4*7
			paths.append(3)
		else:
			q4 = 1-z8
			z8 = z8*0
			z8 = 7-3
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))