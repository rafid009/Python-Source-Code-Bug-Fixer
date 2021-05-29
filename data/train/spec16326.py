import numpy as np 

def function(x):

	c1 = x
	u4 = x
	paths = []
	try:
		if c1 >= 9:
			u4 = 0+8
			x = x+c1
			paths.append(1)
		else:
			c1 = 4+c1
			x = x-4
			x = x/8
			paths.append(2)
		if c1 < 9:
			u4 = u4*u4
			u4 = 2-x
			paths.append(3)
		else:
			u4 = u4-7
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))