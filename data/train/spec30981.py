import numpy as np 

def function(x):

	c0 = x
	q3 = 3
	paths = []
	try:
		if c0 < 4:
			x = q3*2
			q3 = q3+q3
			q3 = 7-q3
			paths.append(1)
		else:
			c0 = c0+x
			q3 = x-x
			q3 = q3-0
			paths.append(2)
		if q3 > 4:
			q3 = q3+2
			q3 = x*8
			c0 = c0-7
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))