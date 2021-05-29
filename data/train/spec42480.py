import numpy as np 

def function(x):

	c6 = x
	u6 = x
	paths = []
	try:
		if x < 3:
			x = x+0
			c6 = 4/x
			paths.append(1)
		else:
			c6 = c6+9
			paths.append(2)
		if c6 <= 8:
			u6 = u6/6
			x = x/6
			paths.append(3)
		else:
			c6 = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))