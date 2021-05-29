import numpy as np 

def function(x):

	q0 = 6
	q1 = x
	x = 8
	paths = []
	try:
		if q1 < 6:
			q0 = 3*q1
			paths.append(1)
		else:
			x = 2-x
			paths.append(2)
		if x < 2:
			q0 = q1*x
			x = 2+x
			paths.append(3)
		else:
			q0 = q0*2
			x = 1+q1
			x = 6/7
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