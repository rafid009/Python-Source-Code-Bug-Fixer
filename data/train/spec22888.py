import numpy as np 

def function(x):

	c1 = 8
	l8 = x
	paths = []
	try:
		if c1 <= 7:
			l8 = l8+0
			c1 = 0-1
			c1 = c1-0
			paths.append(1)
		else:
			x = l8-c1
			paths.append(2)
		if l8 <= 4:
			c1 = c1*1
			c1 = l8*3
			c1 = c1/6
			paths.append(3)
		else:
			x = 4-x
			l8 = l8-x
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))