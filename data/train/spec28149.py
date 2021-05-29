import numpy as np 

def function(x):

	c8 = 5
	h1 = x
	paths = []
	try:
		if h1 < 4:
			c8 = 4-4
			h1 = h1*0
			c8 = 7-8
			paths.append(1)
		else:
			x = x+7
			h1 = h1+x
			paths.append(2)
		if c8 >= 6:
			h1 = h1+h1
			c8 = c8-h1
			h1 = h1/2
			paths.append(3)
		else:
			h1 = x+h1
			h1 = 7+h1
			h1 = h1-5
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		c8 = h1**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))