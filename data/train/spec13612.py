import numpy as np 

def function(x):

	q6 = x
	z5 = x
	paths = []
	try:
		if x > 1:
			q6 = q6*6
			x = q6+2
			q6 = 0+q6
			paths.append(1)
		else:
			q6 = 2-4
			x = 6+x
			z5 = 1/z5
			paths.append(2)
		if q6 <= 8:
			x = z5-x
			paths.append(3)
		else:
			x = x-q6
			q6 = x+q6
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))