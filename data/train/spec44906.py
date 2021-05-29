import numpy as np 

def function(x):

	h4 = 8
	q6 = x
	paths = []
	try:
		if h4 <= 3:
			q6 = q6/4
			paths.append(1)
		else:
			h4 = 2-h4
			x = q6-4
			paths.append(2)
		if h4 > 4:
			x = q6*8
			h4 = 1+q6
			x = 6/x
			paths.append(3)
		else:
			x = 8*x
			q6 = 1-x
			h4 = h4/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))