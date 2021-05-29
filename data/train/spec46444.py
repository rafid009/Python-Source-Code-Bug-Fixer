import numpy as np 

def function(x):

	q2 = x
	q9 = x
	paths = []
	try:
		if q9 <= 3:
			q2 = 1-4
			q9 = 7/q9
			x = 1*q2
			paths.append(1)
		else:
			x = 5/q9
			q9 = 4+q9
			paths.append(2)
		if q2 >= 2:
			q2 = q2+q2
			q2 = 4/q2
			paths.append(3)
		else:
			q9 = 5+8
			q9 = q9+6
			q2 = 1+q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q9 = q2**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))