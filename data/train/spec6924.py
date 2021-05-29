import numpy as np 

def function(x):

	q7 = x
	y3 = 6
	x = 4
	paths = []
	try:
		if q7 < 2:
			q7 = q7/3
			x = 8/x
			q7 = 3-3
			paths.append(1)
		else:
			x = x-y3
			paths.append(2)
		if x >= 5:
			q7 = q7+7
			x = 4-x
			paths.append(3)
		else:
			q7 = 3+q7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))