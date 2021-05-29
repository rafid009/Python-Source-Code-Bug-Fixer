import numpy as np 

def function(x):

	q5 = 8
	c9 = x
	paths = []
	try:
		if x > 0:
			c9 = 6+4
			c9 = x*c9
			x = 4-9
			paths.append(1)
		else:
			c9 = c9+c9
			x = x-x
			paths.append(2)
		if c9 > 0:
			x = 8-1
			paths.append(3)
		else:
			q5 = c9*q5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))