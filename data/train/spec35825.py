import numpy as np 

def function(x):

	q1 = x
	n8 = 1
	paths = []
	try:
		if q1 >= 6:
			x = x*x
			q1 = q1*1
			q1 = n8*7
			paths.append(1)
		else:
			q1 = 5*6
			paths.append(2)
		if q1 >= 4:
			x = 7-x
			x = x*q1
			paths.append(3)
		else:
			q1 = 6/q1
			n8 = 3-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))