import numpy as np 

def function(x):

	q3 = x
	z5 = x
	paths = []
	try:
		if z5 > 9:
			q3 = 5-3
			q3 = q3+4
			paths.append(1)
		else:
			z5 = 0*z5
			x = 3-x
			paths.append(2)
		if q3 < 6:
			x = x/8
			paths.append(3)
		else:
			z5 = 1/7
			x = q3/9
			z5 = x-7
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))