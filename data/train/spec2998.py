import numpy as np 

def function(x):

	q8 = 7
	u7 = x
	x = x
	paths = []
	try:
		if q8 <= 0:
			u7 = 4*u7
			q8 = 2-q8
			q8 = q8-3
			paths.append(1)
		else:
			u7 = x+3
			paths.append(2)
		if x <= 2:
			x = x-4
			u7 = u7/q8
			paths.append(3)
		else:
			q8 = q8+q8
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