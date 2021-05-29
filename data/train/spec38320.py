import numpy as np 

def function(x):

	q1 = 5
	h3 = 5
	paths = []
	try:
		if q1 >= 7:
			h3 = h3-1
			paths.append(1)
		else:
			q1 = q1*1
			h3 = q1-2
			paths.append(2)
		if q1 < 4:
			x = 0-1
			paths.append(3)
		else:
			q1 = x*6
			h3 = h3-h3
			q1 = 6/q1
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