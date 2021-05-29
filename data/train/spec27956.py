import numpy as np 

def function(x):

	d2 = 7
	q1 = x
	paths = []
	try:
		if q1 >= 4:
			x = 8-x
			paths.append(1)
		else:
			q1 = d2*q1
			q1 = q1*7
			paths.append(2)
		if q1 < 3:
			q1 = q1+5
			paths.append(3)
		else:
			d2 = d2/d2
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))