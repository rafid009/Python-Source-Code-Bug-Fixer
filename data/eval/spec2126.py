import numpy as np 

def function(x):

	q6 = 7
	w4 = 8
	paths = []
	try:
		if x < 9:
			x = 7/x
			q6 = 7-q6
			paths.append(1)
		else:
			q6 = x+8
			w4 = 4/4
			w4 = w4-w4
			paths.append(2)
		if x > 9:
			q6 = q6/7
			q6 = 0-1
			x = x/2
			paths.append(3)
		else:
			x = 2/x
			w4 = x-w4
			w4 = 4-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))