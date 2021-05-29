import numpy as np 

def function(x):

	h4 = 2
	q0 = x
	paths = []
	try:
		if x > 9:
			q0 = 4-4
			paths.append(1)
		else:
			q0 = 7/q0
			q0 = x+q0
			paths.append(2)
		if h4 > 6:
			q0 = 0+q0
			paths.append(3)
		else:
			q0 = q0+q0
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