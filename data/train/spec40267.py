import numpy as np 

def function(x):

	z5 = 3
	q6 = x
	paths = []
	try:
		if q6 <= 1:
			z5 = z5+6
			x = z5/4
			x = x/x
			paths.append(1)
		else:
			z5 = z5-8
			q6 = 6/q6
			x = 1/x
			paths.append(2)
		if x > 4:
			x = x*x
			paths.append(3)
		else:
			z5 = x+z5
			q6 = q6+6
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		q6 = z5**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))