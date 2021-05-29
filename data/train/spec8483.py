import numpy as np 

def function(x):

	q1 = 1
	x1 = x
	paths = []
	try:
		if x < 2:
			x = q1-q1
			x = x+8
			x1 = 9/x1
			paths.append(1)
		else:
			x = x+1
			x = x+8
			paths.append(2)
		if x1 > 4:
			q1 = 7+4
			x = x/7
			x = x-q1
			paths.append(3)
		else:
			x = 4/x
			q1 = q1/q1
			x1 = 4*x1
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		q1 = x1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))