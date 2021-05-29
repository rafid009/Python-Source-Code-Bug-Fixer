import numpy as np 

def function(x):

	c3 = x
	q7 = 0
	paths = []
	try:
		if x >= 6:
			q7 = q7-1
			x = x+q7
			q7 = q7-4
			paths.append(1)
		else:
			q7 = q7/7
			c3 = 0*c3
			q7 = c3+q7
			paths.append(2)
		if x >= 7:
			c3 = c3+q7
			x = 5-x
			paths.append(3)
		else:
			c3 = 2*c3
			c3 = 5/7
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