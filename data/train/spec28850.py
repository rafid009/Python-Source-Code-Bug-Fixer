import numpy as np 

def function(x):

	c4 = 1
	q8 = 4
	paths = []
	try:
		if q8 < 3:
			x = x*7
			x = x/q8
			q8 = q8/9
			paths.append(1)
		else:
			q8 = x/8
			paths.append(2)
		if x < 2:
			q8 = q8*q8
			c4 = 5*c4
			c4 = c4-8
			paths.append(3)
		else:
			x = x+6
			x = 1+5
			q8 = q8*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))