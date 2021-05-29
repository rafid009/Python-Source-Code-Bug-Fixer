import numpy as np 

def function(x):

	q2 = 9
	w7 = x
	paths = []
	try:
		if x >= 8:
			w7 = 9/w7
			paths.append(1)
		else:
			q2 = w7-4
			w7 = w7-5
			x = 7*x
			paths.append(2)
		if q2 < 5:
			x = 8*x
			q2 = w7-x
			w7 = 8*w7
			paths.append(3)
		else:
			q2 = 5/x
			w7 = 3+5
			q2 = q2*q2
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