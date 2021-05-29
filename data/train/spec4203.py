import numpy as np 

def function(x):

	l6 = x
	q1 = 7
	paths = []
	try:
		if q1 >= 8:
			q1 = q1+l6
			l6 = x-l6
			paths.append(1)
		else:
			l6 = 4+l6
			x = x*l6
			paths.append(2)
		if q1 < 6:
			q1 = x/6
			q1 = l6*q1
			q1 = 3-6
			paths.append(3)
		else:
			q1 = 1/l6
			x = 3/l6
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))