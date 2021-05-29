import numpy as np 

def function(x):

	q3 = 6
	e2 = x
	paths = []
	try:
		if q3 >= 0:
			e2 = q3/x
			paths.append(1)
		else:
			q3 = 1/q3
			e2 = e2+3
			paths.append(2)
		if x >= 6:
			q3 = 0-q3
			paths.append(3)
		else:
			e2 = e2+5
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