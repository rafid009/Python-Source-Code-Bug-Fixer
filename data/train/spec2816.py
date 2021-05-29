import numpy as np 

def function(x):

	c4 = x
	n4 = x
	paths = []
	try:
		if x < 2:
			x = x-x
			x = x/n4
			paths.append(1)
		else:
			x = 2/n4
			n4 = n4-n4
			paths.append(2)
		if n4 < 3:
			c4 = 2-c4
			paths.append(3)
		else:
			n4 = c4/n4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))