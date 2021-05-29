import numpy as np 

def function(x):

	q6 = 9
	w4 = x
	paths = []
	try:
		if w4 > 9:
			q6 = q6-8
			paths.append(1)
		else:
			x = x*6
			w4 = x/q6
			paths.append(2)
		if w4 < 1:
			q6 = q6/2
			w4 = w4+w4
			paths.append(3)
		else:
			q6 = 7+w4
			q6 = 2+5
			q6 = 3+5
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		q6 = w4**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))