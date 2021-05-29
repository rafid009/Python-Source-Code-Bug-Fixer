import numpy as np 

def function(x):

	q7 = 0
	n0 = x
	paths = []
	try:
		if q7 >= 0:
			n0 = 4+n0
			q7 = q7/2
			q7 = x/6
			paths.append(1)
		else:
			n0 = 4+2
			q7 = n0-8
			n0 = n0+5
			paths.append(2)
		if n0 > 4:
			x = x-4
			q7 = 5-q7
			q7 = q7/q7
			paths.append(3)
		else:
			q7 = q7-5
			x = 4-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))