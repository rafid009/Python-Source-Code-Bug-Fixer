import numpy as np 

def function(x):

	q1 = 2
	h2 = 8
	paths = []
	try:
		if q1 >= 9:
			h2 = h2-7
			paths.append(1)
		else:
			q1 = h2-q1
			paths.append(2)
		if h2 < 3:
			x = 9/7
			q1 = q1/6
			paths.append(3)
		else:
			q1 = 4/q1
			q1 = q1-h2
			h2 = 7/3
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))