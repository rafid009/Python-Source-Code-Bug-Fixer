import numpy as np 

def function(x):

	z5 = x
	q4 = 9
	paths = []
	try:
		if x > 1:
			z5 = 2+9
			q4 = q4-3
			q4 = x-0
			paths.append(1)
		else:
			z5 = q4/x
			z5 = 2/4
			x = x+z5
			paths.append(2)
		if q4 <= 0:
			x = x-6
			paths.append(3)
		else:
			z5 = z5+x
			z5 = x/z5
			z5 = q4*z5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		q4 = z5**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))