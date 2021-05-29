import numpy as np 

def function(x):

	c0 = 2
	q8 = 4
	paths = []
	try:
		if c0 > 0:
			x = x/c0
			c0 = c0/q8
			paths.append(1)
		else:
			x = x-7
			c0 = 8-1
			x = x+2
			paths.append(2)
		if q8 < 3:
			x = x+x
			paths.append(3)
		else:
			c0 = c0/x
			c0 = c0-x
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		q8 = c0**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))