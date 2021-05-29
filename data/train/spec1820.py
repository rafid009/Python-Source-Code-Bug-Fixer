import numpy as np 

def function(x):

	q0 = 9
	q1 = x
	x = x
	paths = []
	try:
		if q1 < 1:
			q1 = 3*q1
			x = 2-2
			paths.append(1)
		else:
			q1 = q1-6
			q1 = q1/9
			x = x-0
			paths.append(2)
		if x > 8:
			x = 2-x
			q1 = q1+q1
			paths.append(3)
		else:
			q0 = q0-3
			q0 = q1/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))