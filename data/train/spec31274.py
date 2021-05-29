import numpy as np 

def function(x):

	c2 = x
	c5 = 4
	paths = []
	try:
		if c5 <= 0:
			c2 = 8+x
			c5 = 4+c5
			paths.append(1)
		else:
			c2 = c2-9
			paths.append(2)
		if x > 5:
			c2 = c2+2
			paths.append(3)
		else:
			c5 = c2/2
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