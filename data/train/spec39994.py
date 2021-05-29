import numpy as np 

def function(x):

	c2 = x
	t1 = x
	paths = []
	try:
		if c2 < 3:
			c2 = c2+6
			paths.append(1)
		else:
			c2 = 3/4
			paths.append(2)
		if t1 >= 2:
			c2 = 4+0
			x = x*6
			x = 3*x
			paths.append(3)
		else:
			c2 = 4+c2
			x = c2*x
			c2 = c2-3
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		c2 = t1**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))