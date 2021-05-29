import numpy as np 

def function(x):

	q7 = 3
	q0 = 0
	x = x
	paths = []
	try:
		if q7 > 7:
			x = 9+x
			q0 = 9+q0
			q7 = q0-q7
			paths.append(1)
		else:
			q7 = q7/q7
			paths.append(2)
		if x < 7:
			q7 = 8*q7
			x = 4/x
			paths.append(3)
		else:
			q0 = 8+q0
			q0 = 3+0
			q0 = q7-q0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))