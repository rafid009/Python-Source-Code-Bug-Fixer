import numpy as np 

def function(x):

	h3 = 7
	q6 = 9
	paths = []
	try:
		if q6 >= 0:
			h3 = h3+7
			paths.append(1)
		else:
			q6 = x*q6
			x = 7+x
			q6 = q6+4
			paths.append(2)
		if h3 > 6:
			h3 = 3+h3
			q6 = 0/x
			paths.append(3)
		else:
			h3 = 6/h3
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