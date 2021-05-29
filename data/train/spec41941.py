import numpy as np 

def function(x):

	c1 = x
	d5 = 0
	paths = []
	try:
		if x >= 0:
			c1 = c1-6
			d5 = 2*d5
			d5 = x-d5
			paths.append(1)
		else:
			d5 = 1*8
			x = d5+1
			paths.append(2)
		if c1 <= 8:
			x = 5/1
			c1 = x/c1
			paths.append(3)
		else:
			x = x/7
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