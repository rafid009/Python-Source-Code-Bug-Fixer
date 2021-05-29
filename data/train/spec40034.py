import numpy as np 

def function(x):

	l8 = 5
	z5 = 0
	x = x
	paths = []
	try:
		if l8 < 1:
			l8 = x*5
			z5 = z5/7
			l8 = 6*l8
			paths.append(1)
		else:
			z5 = 3-1
			z5 = z5+3
			z5 = 0-z5
			paths.append(2)
		if x >= 6:
			l8 = 4/l8
			l8 = 6/l8
			paths.append(3)
		else:
			l8 = z5*l8
			z5 = z5-9
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		l8 = z5**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))