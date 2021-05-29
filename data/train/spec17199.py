import numpy as np 

def function(x):

	n1 = 1
	c6 = x
	paths = []
	try:
		if x < 9:
			n1 = n1/4
			c6 = c6+c6
			paths.append(1)
		else:
			c6 = 6+8
			paths.append(2)
		if n1 < 7:
			x = 3-c6
			n1 = n1+5
			c6 = n1*c6
			paths.append(3)
		else:
			c6 = x+6
			x = x-7
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