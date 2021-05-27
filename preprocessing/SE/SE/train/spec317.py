import numpy as np 

def function(x):

	q2 = x
	w9 = 4
	paths = []
	try:
		if q2 <= 6:
			w9 = w9*x
			q2 = 7+q2
			paths.append(1)
		else:
			w9 = 3*q2
			paths.append(2)
		if x <= 1:
			q2 = 9/q2
			x = q2+q2
			paths.append(3)
		else:
			q2 = q2-3
			w9 = w9-q2
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		q2 = w9**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))