import numpy as np 

def function(x):

	q7 = 3
	o8 = 3
	paths = []
	try:
		if q7 < 8:
			q7 = q7/6
			paths.append(1)
		else:
			x = x/o8
			o8 = q7+o8
			x = 0*x
			paths.append(2)
		if x >= 0:
			o8 = o8/6
			paths.append(3)
		else:
			q7 = 4-q7
			q7 = 6-7
			q7 = q7+5
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