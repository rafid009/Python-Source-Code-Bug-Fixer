import numpy as np 

def function(x):

	c8 = x
	u4 = 4
	paths = []
	try:
		if u4 < 1:
			x = x-u4
			u4 = x+x
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if c8 >= 9:
			c8 = x/c8
			x = c8*x
			c8 = c8/c8
			paths.append(3)
		else:
			u4 = u4/8
			u4 = u4+0
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))