import numpy as np 

def function(x):

	q4 = x
	r9 = 3
	paths = []
	try:
		if x < 8:
			r9 = r9*q4
			paths.append(1)
		else:
			x = 4/x
			paths.append(2)
		if x <= 0:
			x = 9-1
			paths.append(3)
		else:
			q4 = q4/5
			q4 = q4-r9
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