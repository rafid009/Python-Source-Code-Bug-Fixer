import numpy as np 

def function(x):

	q6 = x
	w2 = 7
	paths = []
	try:
		if q6 >= 2:
			x = 3/x
			w2 = w2/q6
			paths.append(1)
		else:
			w2 = 9/q6
			paths.append(2)
		if w2 <= 6:
			x = x/5
			w2 = q6*w2
			w2 = 1-w2
			paths.append(3)
		else:
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		q6 = w2**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))