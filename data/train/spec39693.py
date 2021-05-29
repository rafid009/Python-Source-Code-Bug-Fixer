import numpy as np 

def function(x):

	q0 = x
	x7 = 8
	paths = []
	try:
		if x >= 7:
			x7 = 0+x7
			x7 = x7/1
			paths.append(1)
		else:
			x = 7+x
			q0 = q0/1
			paths.append(2)
		if q0 >= 8:
			x = x-0
			x7 = x7-4
			paths.append(3)
		else:
			x7 = x7-x
			x = 8/x
			x = q0-x
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))