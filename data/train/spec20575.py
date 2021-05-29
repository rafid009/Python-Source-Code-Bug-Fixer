import numpy as np 

def function(x):

	u8 = 5
	c1 = 4
	paths = []
	try:
		if u8 < 9:
			x = 1+x
			u8 = 1+u8
			u8 = 0+x
			paths.append(1)
		else:
			c1 = 6-4
			c1 = c1*u8
			c1 = c1+0
			paths.append(2)
		if x <= 7:
			u8 = 9*u8
			c1 = 1/8
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		c1 = u8**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))