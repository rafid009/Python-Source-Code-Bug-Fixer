import numpy as np 

def function(x):

	c2 = 2
	q6 = x
	paths = []
	try:
		if c2 <= 0:
			q6 = x*c2
			x = x+4
			x = x*1
			paths.append(1)
		else:
			q6 = 3/q6
			x = 7+x
			q6 = 1/8
			paths.append(2)
		if x <= 3:
			c2 = 8/c2
			x = 6-x
			paths.append(3)
		else:
			q6 = 8+q6
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))