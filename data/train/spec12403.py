import numpy as np 

def function(x):

	c8 = 3
	t4 = x
	paths = []
	try:
		if x < 3:
			x = x*0
			x = x/c8
			paths.append(1)
		else:
			t4 = t4+t4
			paths.append(2)
		if c8 >= 3:
			c8 = 4*c8
			x = 0*t4
			x = x-x
			paths.append(3)
		else:
			c8 = c8*2
			t4 = t4-2
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		c8 = t4**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))