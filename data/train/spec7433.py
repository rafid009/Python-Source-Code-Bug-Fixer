import numpy as np 

def function(x):

	c4 = x
	x4 = x
	x = 2
	paths = []
	try:
		if x < 6:
			x4 = 2-5
			x = x4/7
			paths.append(1)
		else:
			x = 4/x
			c4 = 5/c4
			paths.append(2)
		if x >= 3:
			x4 = 9*x4
			c4 = c4*2
			paths.append(3)
		else:
			c4 = 9/x
			x4 = x4*9
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x4 = c4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))