import numpy as np 

def function(x):

	c3 = x
	w4 = 1
	x = x
	paths = []
	try:
		if c3 > 3:
			w4 = w4-7
			w4 = 0*w4
			paths.append(1)
		else:
			w4 = 4+c3
			c3 = c3*3
			paths.append(2)
		if c3 <= 3:
			c3 = x-1
			x = 7+9
			c3 = c3-8
			paths.append(3)
		else:
			c3 = c3+c3
			w4 = 5+8
			c3 = c3*0
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		c3 = w4**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))