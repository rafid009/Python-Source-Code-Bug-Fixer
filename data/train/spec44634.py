import numpy as np 

def function(x):

	u9 = x
	c2 = x
	paths = []
	try:
		if x > 9:
			x = 5*x
			x = c2+8
			paths.append(1)
		else:
			u9 = 7/u9
			x = 2+x
			paths.append(2)
		if x > 6:
			u9 = u9*7
			c2 = c2*9
			paths.append(3)
		else:
			c2 = 4/c2
			u9 = u9*3
			c2 = 7-c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))