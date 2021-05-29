import numpy as np 

def function(x):

	q1 = x
	w1 = 0
	paths = []
	try:
		if q1 > 5:
			w1 = 8*w1
			x = 1*8
			paths.append(1)
		else:
			x = q1*3
			w1 = 4*q1
			q1 = q1/9
			paths.append(2)
		if q1 > 3:
			x = w1/5
			paths.append(3)
		else:
			w1 = 6*w1
			q1 = q1+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))