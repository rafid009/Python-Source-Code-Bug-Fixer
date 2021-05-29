import numpy as np 

def function(x):

	q3 = x
	z5 = x
	paths = []
	try:
		if x >= 9:
			q3 = 0+q3
			paths.append(1)
		else:
			z5 = q3/7
			z5 = q3/7
			x = 1-x
			paths.append(2)
		if x > 7:
			z5 = x-0
			q3 = 6-z5
			q3 = z5/x
			paths.append(3)
		else:
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))