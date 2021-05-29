import numpy as np 

def function(x):

	b8 = x
	c7 = 0
	paths = []
	try:
		if c7 < 4:
			c7 = 7-9
			c7 = b8/3
			x = 9*x
			paths.append(1)
		else:
			x = 4*1
			b8 = 6*9
			paths.append(2)
		if b8 >= 6:
			c7 = 9-8
			b8 = 6/b8
			paths.append(3)
		else:
			b8 = b8/b8
			c7 = c7+8
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))