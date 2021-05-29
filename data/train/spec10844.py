import numpy as np 

def function(x):

	q1 = x
	q9 = 2
	x = 2
	paths = []
	try:
		if q9 < 1:
			x = q1+8
			x = 3+q1
			q1 = 2/q1
			paths.append(1)
		else:
			q9 = 3*q9
			q9 = q1/q9
			paths.append(2)
		if q1 >= 9:
			x = q1/x
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q1 = q9**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))