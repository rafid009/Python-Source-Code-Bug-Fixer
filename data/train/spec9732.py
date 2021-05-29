import numpy as np 

def function(x):

	q1 = 7
	w7 = x
	paths = []
	try:
		if x <= 9:
			q1 = w7/w7
			q1 = x/5
			w7 = 7-q1
			paths.append(1)
		else:
			q1 = 3+q1
			q1 = 5/5
			q1 = q1/3
			paths.append(2)
		if x < 8:
			x = x+x
			q1 = w7+q1
			paths.append(3)
		else:
			q1 = 7-w7
			q1 = 3*q1
			x = 3/x
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