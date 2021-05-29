import numpy as np 

def function(x):

	c8 = x
	i4 = x
	paths = []
	try:
		if c8 <= 9:
			i4 = c8+9
			x = x+2
			x = x/c8
			paths.append(1)
		else:
			i4 = 2*0
			paths.append(2)
		if x >= 5:
			c8 = c8+1
			i4 = i4*5
			x = 4+0
			paths.append(3)
		else:
			x = 5/2
			c8 = 4/c8
			i4 = x*i4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		c8 = i4**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))