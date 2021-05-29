import numpy as np 

def function(x):

	q8 = 6
	q3 = x
	paths = []
	try:
		if q8 <= 9:
			x = 4+2
			q8 = q8-4
			q8 = q3/q3
			paths.append(1)
		else:
			q8 = q8-5
			paths.append(2)
		if q3 < 6:
			q8 = q8/6
			q8 = 4/q8
			q3 = q3+x
			paths.append(3)
		else:
			q3 = q3*q3
			x = q8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))