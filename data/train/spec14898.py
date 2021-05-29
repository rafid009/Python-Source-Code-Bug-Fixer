import numpy as np 

def function(x):

	f1 = 7
	q7 = x
	paths = []
	try:
		if q7 > 9:
			f1 = x-f1
			x = x*3
			f1 = f1*q7
			paths.append(1)
		else:
			q7 = 8/q7
			x = x-f1
			q7 = q7-x
			paths.append(2)
		if q7 > 0:
			q7 = 0-q7
			paths.append(3)
		else:
			x = 7-x
			q7 = f1*0
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