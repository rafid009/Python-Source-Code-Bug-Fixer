import numpy as np 

def function(x):

	f5 = x
	c8 = x
	paths = []
	try:
		if f5 > 3:
			f5 = f5/1
			x = x+7
			paths.append(1)
		else:
			f5 = f5*7
			x = c8+x
			paths.append(2)
		if c8 >= 7:
			x = c8-x
			c8 = 0*2
			paths.append(3)
		else:
			c8 = 2/c8
			f5 = f5+9
			x = c8*7
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		c8 = c8**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))