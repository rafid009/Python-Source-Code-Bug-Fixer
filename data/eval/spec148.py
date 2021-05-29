import numpy as np 

def function(x):

	c9 = x
	n5 = 6
	paths = []
	try:
		if x <= 8:
			n5 = 9/n5
			c9 = 1*c9
			paths.append(1)
		else:
			n5 = n5-4
			x = x-7
			c9 = c9/x
			paths.append(2)
		if c9 <= 5:
			n5 = n5-n5
			x = 8+n5
			paths.append(3)
		else:
			x = x+6
			n5 = n5*1
			c9 = n5-x
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))