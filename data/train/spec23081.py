import numpy as np 

def function(x):

	c6 = 1
	t6 = 2
	paths = []
	try:
		if x <= 2:
			c6 = c6/3
			x = x-4
			paths.append(1)
		else:
			t6 = 7-t6
			paths.append(2)
		if x > 4:
			t6 = 3+5
			c6 = 1/c6
			c6 = c6-x
			paths.append(3)
		else:
			t6 = t6-x
			x = 8*3
			c6 = c6-c6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))