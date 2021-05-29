import numpy as np 

def function(x):

	q1 = x
	q2 = 9
	paths = []
	try:
		if x <= 3:
			q1 = 5/x
			q2 = q2-q2
			paths.append(1)
		else:
			q2 = 9-1
			x = x*x
			q1 = 3+q1
			paths.append(2)
		if q2 >= 0:
			q1 = 9-q1
			q2 = 0-6
			q2 = q2-2
			paths.append(3)
		else:
			q1 = 3*9
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q2 = q1**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))