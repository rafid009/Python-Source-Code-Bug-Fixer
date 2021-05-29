import numpy as np 

def function(x):

	z5 = x
	q4 = x
	paths = []
	try:
		if z5 >= 4:
			q4 = q4+7
			paths.append(1)
		else:
			q4 = 1-2
			z5 = z5-6
			paths.append(2)
		if q4 < 4:
			q4 = x/3
			paths.append(3)
		else:
			x = x+x
			x = x-6
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