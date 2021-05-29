import numpy as np 

def function(x):

	r3 = x
	q1 = 1
	paths = []
	try:
		if r3 > 0:
			r3 = r3*6
			x = q1/7
			paths.append(1)
		else:
			r3 = q1/r3
			r3 = r3*r3
			q1 = q1-4
			paths.append(2)
		if q1 > 2:
			q1 = 1*3
			q1 = 8*q1
			r3 = q1/7
			paths.append(3)
		else:
			q1 = q1*1
			q1 = r3*r3
			r3 = r3/4
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