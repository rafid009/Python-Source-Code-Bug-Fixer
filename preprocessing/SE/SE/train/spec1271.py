import numpy as np 

def function(x):

	c8 = x
	v9 = 2
	paths = []
	try:
		if c8 < 4:
			v9 = 9+v9
			paths.append(1)
		else:
			v9 = v9*1
			v9 = v9+7
			paths.append(2)
		if x >= 9:
			c8 = 0*4
			c8 = c8*c8
			v9 = 3-v9
			paths.append(3)
		else:
			v9 = 8-v9
			x = x+x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		c8 = v9**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))