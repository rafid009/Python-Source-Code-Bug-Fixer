import numpy as np 

def function(x):

	c2 = x
	q8 = x
	paths = []
	try:
		if q8 <= 5:
			q8 = q8*q8
			q8 = 1/x
			x = x-c2
			paths.append(1)
		else:
			q8 = c2*q8
			paths.append(2)
		if c2 <= 2:
			c2 = c2*4
			c2 = c2-q8
			x = x+x
			paths.append(3)
		else:
			c2 = c2-4
			c2 = 5/c2
			q8 = 7-2
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))