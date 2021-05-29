import numpy as np 

def function(x):

	q7 = 9
	q8 = x
	paths = []
	try:
		if x > 6:
			x = 6*q7
			x = x/q7
			q7 = q7/6
			paths.append(1)
		else:
			x = 8-6
			paths.append(2)
		if q7 < 0:
			q7 = q7/q7
			x = x+x
			q8 = 9/x
			paths.append(3)
		else:
			q8 = 0-5
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q7 = q8**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))