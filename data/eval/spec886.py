import numpy as np 

def function(x):

	s2 = x
	c8 = 6
	paths = []
	try:
		if c8 < 7:
			c8 = x*2
			x = x+7
			x = x*x
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if s2 >= 0:
			c8 = c8+x
			c8 = 5*9
			paths.append(3)
		else:
			c8 = c8+8
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		c8 = s2**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))