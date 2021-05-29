import numpy as np 

def function(x):

	q6 = 9
	y7 = x
	paths = []
	try:
		if q6 >= 9:
			x = x*y7
			q6 = q6-y7
			paths.append(1)
		else:
			q6 = q6*4
			x = x/q6
			y7 = 9+y7
			paths.append(2)
		if q6 < 9:
			y7 = y7-0
			q6 = 0-q6
			paths.append(3)
		else:
			q6 = q6+y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))