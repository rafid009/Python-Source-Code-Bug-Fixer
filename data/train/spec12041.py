import numpy as np 

def function(x):

	c6 = x
	n8 = 6
	paths = []
	try:
		if c6 <= 2:
			c6 = x-0
			n8 = n8+8
			c6 = c6+c6
			paths.append(1)
		else:
			n8 = n8+x
			x = x+2
			c6 = 0/4
			paths.append(2)
		if c6 >= 2:
			x = 3-x
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))