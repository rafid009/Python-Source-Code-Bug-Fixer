import numpy as np 

def function(x):

	c2 = x
	l5 = x
	paths = []
	try:
		if c2 < 6:
			x = 7-x
			l5 = 5*7
			l5 = c2/9
			paths.append(1)
		else:
			l5 = 5/l5
			l5 = 7/l5
			c2 = c2+x
			paths.append(2)
		if x <= 3:
			x = x*2
			x = x-l5
			l5 = c2+l5
			paths.append(3)
		else:
			l5 = l5/4
			x = x+8
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		c2 = l5**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))