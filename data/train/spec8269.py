import numpy as np 

def function(x):

	f7 = x
	c1 = x
	x = 5
	paths = []
	try:
		if f7 <= 0:
			x = 4*x
			c1 = c1+7
			paths.append(1)
		else:
			c1 = c1-4
			x = x+5
			paths.append(2)
		if c1 > 6:
			x = f7/7
			x = 2/f7
			f7 = 2*f7
			paths.append(3)
		else:
			x = 4-c1
			c1 = f7*9
			x = 6*7
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))