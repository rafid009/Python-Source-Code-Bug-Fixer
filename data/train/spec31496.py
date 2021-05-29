import numpy as np 

def function(x):

	f2 = 8
	c2 = x
	paths = []
	try:
		if x <= 4:
			x = x/3
			c2 = 1/c2
			c2 = 6+c2
			paths.append(1)
		else:
			x = x-8
			c2 = x/1
			paths.append(2)
		if x >= 1:
			f2 = 1-f2
			x = x+f2
			paths.append(3)
		else:
			c2 = c2/c2
			f2 = f2*f2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		c2 = f2**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))