import numpy as np 

def function(x):

	q2 = x
	w8 = 5
	paths = []
	try:
		if x < 2:
			w8 = 6*w8
			w8 = w8-x
			x = x-w8
			paths.append(1)
		else:
			w8 = 5/x
			q2 = q2-q2
			q2 = 1+q2
			paths.append(2)
		if x <= 8:
			q2 = 3*q2
			x = x*6
			paths.append(3)
		else:
			q2 = w8/q2
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))