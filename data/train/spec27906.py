import numpy as np 

def function(x):

	q4 = 0
	c4 = x
	paths = []
	try:
		if x < 8:
			x = x+x
			x = 6+q4
			q4 = q4/8
			paths.append(1)
		else:
			x = 3-x
			q4 = c4*x
			paths.append(2)
		if x < 4:
			c4 = c4*0
			q4 = x-3
			paths.append(3)
		else:
			x = q4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))