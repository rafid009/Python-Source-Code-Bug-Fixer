import numpy as np 

def function(x):

	c8 = 3
	x5 = x
	paths = []
	try:
		if c8 <= 9:
			x = 8+6
			x = x-x
			x = x/x5
			paths.append(1)
		else:
			x = 7-x
			x5 = c8+x
			paths.append(2)
		if c8 <= 1:
			x5 = x5/7
			x5 = x5+9
			paths.append(3)
		else:
			x5 = x-x5
			c8 = 6+x
			c8 = c8/x5
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x5 = c8**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))