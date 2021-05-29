import numpy as np 

def function(x):

	n7 = 2
	c9 = x
	paths = []
	try:
		if n7 <= 9:
			n7 = n7*1
			paths.append(1)
		else:
			x = x+c9
			c9 = c9-0
			n7 = n7*4
			paths.append(2)
		if x > 0:
			c9 = 8/1
			x = 2/x
			n7 = 4*c9
			paths.append(3)
		else:
			c9 = n7-3
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