import numpy as np 

def function(x):

	c6 = 6
	l5 = x
	paths = []
	try:
		if x >= 0:
			l5 = l5/9
			l5 = x*1
			x = x-c6
			paths.append(1)
		else:
			l5 = l5/c6
			c6 = 7/l5
			c6 = 8-c6
			paths.append(2)
		if c6 > 3:
			c6 = 2*c6
			paths.append(3)
		else:
			l5 = l5-7
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))