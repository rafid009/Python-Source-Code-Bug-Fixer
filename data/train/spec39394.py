import numpy as np 

def function(x):

	q7 = x
	c4 = 9
	paths = []
	try:
		if x < 7:
			x = 1+8
			paths.append(1)
		else:
			c4 = c4-6
			x = c4-0
			paths.append(2)
		if q7 < 9:
			c4 = 8-c4
			x = x-5
			q7 = q7*9
			paths.append(3)
		else:
			q7 = q7/q7
			c4 = 6/c4
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