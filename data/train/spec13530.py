import numpy as np 

def function(x):

	c0 = x
	l1 = 8
	paths = []
	try:
		if x >= 9:
			x = x*5
			paths.append(1)
		else:
			c0 = c0+c0
			l1 = l1/l1
			paths.append(2)
		if x < 1:
			l1 = l1*2
			paths.append(3)
		else:
			l1 = x-l1
			l1 = l1+l1
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