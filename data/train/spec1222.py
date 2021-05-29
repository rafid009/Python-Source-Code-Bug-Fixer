import numpy as np 

def function(x):

	c1 = 2
	c5 = 5
	paths = []
	try:
		if c1 < 6:
			c5 = 7*c5
			c5 = x*5
			x = x-0
			paths.append(1)
		else:
			c5 = c5*4
			c5 = 2*c5
			paths.append(2)
		if c1 < 5:
			c1 = c1/x
			paths.append(3)
		else:
			c1 = c5+c1
			c5 = c5+x
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		x = c5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))