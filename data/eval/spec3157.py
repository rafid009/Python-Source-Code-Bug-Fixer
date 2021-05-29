import numpy as np 

def function(x):

	n5 = 2
	c7 = x
	paths = []
	try:
		if x < 5:
			x = x*8
			x = 1+x
			paths.append(1)
		else:
			x = c7/6
			c7 = c7*6
			paths.append(2)
		if n5 <= 3:
			n5 = n5/9
			c7 = c7+0
			paths.append(3)
		else:
			c7 = c7-c7
			c7 = x/x
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		c7 = c7**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))