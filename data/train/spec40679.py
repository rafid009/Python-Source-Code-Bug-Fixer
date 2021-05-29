import numpy as np 

def function(x):

	t7 = 4
	c8 = 9
	paths = []
	try:
		if t7 >= 2:
			c8 = 3*8
			x = 1/x
			paths.append(1)
		else:
			c8 = 6+3
			t7 = t7-8
			t7 = t7/7
			paths.append(2)
		if t7 > 7:
			x = 7-2
			t7 = 0+t7
			paths.append(3)
		else:
			c8 = 8/x
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