import numpy as np 

def function(x):

	w4 = 9
	q1 = x
	paths = []
	try:
		if w4 > 7:
			q1 = q1/1
			paths.append(1)
		else:
			x = 6*x
			q1 = 5+q1
			paths.append(2)
		if x <= 6:
			w4 = 7*w4
			paths.append(3)
		else:
			w4 = 1*5
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