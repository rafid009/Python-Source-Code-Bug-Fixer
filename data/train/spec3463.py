import numpy as np 

def function(x):

	e2 = x
	q3 = 3
	paths = []
	try:
		if q3 >= 0:
			q3 = 6-q3
			paths.append(1)
		else:
			e2 = 6*6
			q3 = 7/x
			paths.append(2)
		if e2 > 5:
			q3 = 7/q3
			x = x-x
			q3 = q3+q3
			paths.append(3)
		else:
			e2 = 1/e2
			q3 = q3-x
			q3 = q3+q3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))