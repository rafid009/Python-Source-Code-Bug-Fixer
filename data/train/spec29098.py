import numpy as np 

def function(x):

	q4 = x
	x7 = 3
	x = 9
	paths = []
	try:
		if x <= 2:
			x7 = x7+0
			paths.append(1)
		else:
			x7 = x7/x7
			paths.append(2)
		if x7 < 6:
			q4 = 4-q4
			q4 = 9-q4
			paths.append(3)
		else:
			x7 = x7-6
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))