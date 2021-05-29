import numpy as np 

def function(x):

	w4 = 1
	q1 = x
	paths = []
	try:
		if w4 >= 0:
			x = x*5
			w4 = 1/w4
			w4 = q1/x
			paths.append(1)
		else:
			w4 = 8-w4
			q1 = 7/q1
			x = x*x
			paths.append(2)
		if w4 <= 8:
			w4 = x-w4
			w4 = w4*1
			q1 = w4+q1
			paths.append(3)
		else:
			x = x-2
			q1 = q1/3
			q1 = 9-2
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		w4 = q1**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))