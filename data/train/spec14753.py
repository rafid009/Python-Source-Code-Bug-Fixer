import numpy as np 

def function(x):

	c1 = 7
	f5 = x
	paths = []
	try:
		if f5 <= 9:
			x = 4+x
			f5 = 9-f5
			paths.append(1)
		else:
			c1 = 1*9
			x = x*1
			paths.append(2)
		if c1 < 8:
			x = x-2
			x = x-f5
			paths.append(3)
		else:
			c1 = 0-7
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