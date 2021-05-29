import numpy as np 

def function(x):

	q0 = x
	x7 = x
	x = 0
	paths = []
	try:
		if x7 >= 6:
			q0 = q0-5
			x7 = x7+6
			q0 = 7*1
			paths.append(1)
		else:
			q0 = 5+q0
			x7 = x7/8
			q0 = q0*q0
			paths.append(2)
		if x > 1:
			x = x/3
			q0 = q0/x
			paths.append(3)
		else:
			x = 9/5
			x = x/5
			x7 = x7*x
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		q0 = x7**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))