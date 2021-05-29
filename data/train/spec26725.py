import numpy as np 

def function(x):

	c7 = x
	o5 = x
	paths = []
	try:
		if c7 >= 2:
			c7 = 2+3
			c7 = 3*c7
			x = x*2
			paths.append(1)
		else:
			x = 9+6
			c7 = x/c7
			paths.append(2)
		if x < 6:
			c7 = c7+2
			o5 = o5+x
			x = x*9
			paths.append(3)
		else:
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		c7 = o5**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))