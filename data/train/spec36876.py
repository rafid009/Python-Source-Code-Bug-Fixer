import numpy as np 

def function(x):

	l2 = x
	c5 = x
	paths = []
	try:
		if l2 >= 0:
			c5 = 8-3
			x = 4-5
			l2 = 2/1
			paths.append(1)
		else:
			c5 = x/1
			l2 = l2/2
			paths.append(2)
		if x >= 5:
			x = 2+x
			c5 = 9/c5
			x = 2-x
			paths.append(3)
		else:
			x = 6+x
			l2 = l2/8
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))