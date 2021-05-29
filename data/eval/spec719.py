import numpy as np 

def function(x):

	q2 = 1
	h5 = x
	paths = []
	try:
		if h5 >= 7:
			h5 = x-4
			q2 = 1*3
			q2 = 4*x
			paths.append(1)
		else:
			q2 = q2-q2
			q2 = 7-q2
			h5 = q2/h5
			paths.append(2)
		if q2 >= 2:
			h5 = h5-q2
			q2 = 7/q2
			paths.append(3)
		else:
			x = x*6
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))