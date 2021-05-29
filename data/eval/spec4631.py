import numpy as np 

def function(x):

	c7 = 3
	q4 = 5
	paths = []
	try:
		if q4 <= 7:
			q4 = q4-5
			c7 = 2/c7
			paths.append(1)
		else:
			x = c7/8
			x = x*3
			paths.append(2)
		if c7 <= 2:
			q4 = 2*q4
			q4 = q4-1
			c7 = q4-c7
			paths.append(3)
		else:
			q4 = q4-x
			c7 = c7-5
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))