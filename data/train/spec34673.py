import numpy as np 

def function(x):

	c0 = 9
	i8 = x
	paths = []
	try:
		if i8 > 0:
			i8 = 2+8
			x = 0-x
			x = 2+x
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if x >= 3:
			x = 4/7
			c0 = 7+0
			i8 = c0+c0
			paths.append(3)
		else:
			c0 = c0*x
			i8 = i8+5
			i8 = i8+1
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		c0 = i8**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))