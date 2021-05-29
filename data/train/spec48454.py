import numpy as np 

def function(x):

	c0 = 6
	y0 = x
	paths = []
	try:
		if y0 < 7:
			c0 = c0*x
			c0 = y0+5
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if c0 > 4:
			x = 8-8
			x = x+2
			x = x-9
			paths.append(3)
		else:
			y0 = 3/5
			c0 = c0*0
			x = x*x
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))