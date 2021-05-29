import numpy as np 

def function(x):

	c7 = 9
	s8 = 3
	x = 5
	paths = []
	try:
		if c7 >= 3:
			x = s8-c7
			c7 = 3/c7
			paths.append(1)
		else:
			x = 7-x
			c7 = c7*5
			x = x*0
			paths.append(2)
		if x > 4:
			x = 5-x
			x = s8+x
			c7 = c7+s8
			paths.append(3)
		else:
			c7 = 6/c7
			s8 = s8/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))