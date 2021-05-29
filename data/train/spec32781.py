import numpy as np 

def function(x):

	c2 = x
	r3 = 3
	paths = []
	try:
		if r3 > 9:
			c2 = 9*4
			x = x+8
			paths.append(1)
		else:
			c2 = 4-c2
			r3 = 9*r3
			paths.append(2)
		if c2 < 7:
			c2 = 5+c2
			r3 = 4+9
			paths.append(3)
		else:
			x = c2/x
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		c2 = c2**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))