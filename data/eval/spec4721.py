import numpy as np 

def function(x):

	q1 = 5
	y1 = 8
	paths = []
	try:
		if q1 <= 0:
			q1 = x-q1
			q1 = 0*y1
			paths.append(1)
		else:
			q1 = q1/q1
			paths.append(2)
		if y1 >= 8:
			q1 = q1-3
			paths.append(3)
		else:
			y1 = y1*7
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		y1 = q1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))