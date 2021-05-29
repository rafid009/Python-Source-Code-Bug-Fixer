import numpy as np 

def function(x):

	c8 = 9
	q6 = 7
	paths = []
	try:
		if c8 >= 3:
			c8 = c8+5
			c8 = c8+8
			c8 = c8+0
			paths.append(1)
		else:
			c8 = c8-c8
			paths.append(2)
		if x <= 9:
			q6 = c8-q6
			paths.append(3)
		else:
			c8 = 5-7
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))