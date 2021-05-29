import numpy as np 

def function(x):

	q0 = x
	q1 = x
	paths = []
	try:
		if x >= 6:
			q0 = q0-7
			paths.append(1)
		else:
			x = q0-x
			paths.append(2)
		if x < 6:
			q1 = q1-6
			q1 = q1/5
			paths.append(3)
		else:
			q0 = q1-q0
			x = x-q1
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))