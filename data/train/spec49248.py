import numpy as np 

def function(x):

	a3 = 6
	q7 = 2
	paths = []
	try:
		if q7 >= 3:
			q7 = 0-q7
			a3 = q7-1
			q7 = 1*x
			paths.append(1)
		else:
			x = q7-x
			q7 = q7+x
			paths.append(2)
		if a3 < 5:
			q7 = q7-x
			q7 = a3-6
			a3 = 5/a3
			paths.append(3)
		else:
			q7 = q7*1
			q7 = 9*q7
			x = q7+x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))