import numpy as np 

def function(x):

	l4 = x
	c4 = x
	paths = []
	try:
		if l4 > 3:
			c4 = c4+0
			paths.append(1)
		else:
			x = x-9
			x = x-9
			x = x-x
			paths.append(2)
		if x < 0:
			c4 = 1+c4
			x = 1/1
			c4 = l4-8
			paths.append(3)
		else:
			l4 = x-1
			l4 = l4*c4
			c4 = c4-7
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))