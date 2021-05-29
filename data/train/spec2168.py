import numpy as np 

def function(x):

	q6 = 5
	x5 = x
	paths = []
	try:
		if q6 < 5:
			x5 = x5+x5
			paths.append(1)
		else:
			q6 = q6-3
			x5 = 9+8
			paths.append(2)
		if q6 > 1:
			x5 = 2*q6
			q6 = x-9
			paths.append(3)
		else:
			x = x-q6
			x = x-0
			q6 = 6/5
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))