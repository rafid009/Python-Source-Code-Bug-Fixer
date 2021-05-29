import numpy as np 

def function(x):

	c4 = x
	q5 = x
	paths = []
	try:
		if x > 4:
			c4 = x-4
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if x <= 8:
			c4 = 3+c4
			x = 3/x
			q5 = q5+2
			paths.append(3)
		else:
			x = 0-7
			c4 = 6/c4
			q5 = 3-q5
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))