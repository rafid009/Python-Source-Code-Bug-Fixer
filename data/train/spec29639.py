import numpy as np 

def function(x):

	c4 = x
	y0 = x
	paths = []
	try:
		if y0 < 4:
			x = x*c4
			paths.append(1)
		else:
			c4 = c4*0
			y0 = y0*x
			x = x+7
			paths.append(2)
		if y0 <= 4:
			x = x-5
			c4 = 3-1
			c4 = 5/c4
			paths.append(3)
		else:
			y0 = 4*2
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		c4 = y0**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))