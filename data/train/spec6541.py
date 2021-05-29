import numpy as np 

def function(x):

	q1 = x
	w0 = 9
	paths = []
	try:
		if x < 8:
			x = x+7
			paths.append(1)
		else:
			x = x*x
			w0 = w0-q1
			paths.append(2)
		if w0 > 2:
			w0 = x*6
			q1 = 7+w0
			w0 = 7+4
			paths.append(3)
		else:
			w0 = 7-1
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