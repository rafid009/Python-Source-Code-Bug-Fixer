import numpy as np 

def function(x):

	c2 = 3
	u5 = 4
	paths = []
	try:
		if x <= 2:
			c2 = u5-x
			paths.append(1)
		else:
			u5 = x-8
			c2 = 6/x
			u5 = x/u5
			paths.append(2)
		if u5 < 6:
			c2 = c2/8
			c2 = c2*x
			c2 = 1+c2
			paths.append(3)
		else:
			c2 = c2-7
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