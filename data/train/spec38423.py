import numpy as np 

def function(x):

	n1 = 7
	q7 = x
	paths = []
	try:
		if q7 > 7:
			n1 = 4*x
			q7 = 2*q7
			q7 = q7/x
			paths.append(1)
		else:
			x = x*6
			n1 = 1-x
			paths.append(2)
		if x < 0:
			n1 = n1+9
			x = x*x
			x = q7-x
			paths.append(3)
		else:
			q7 = 0-3
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))