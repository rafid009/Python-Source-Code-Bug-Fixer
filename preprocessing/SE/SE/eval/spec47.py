import numpy as np 

def function(x):

	c5 = x
	h8 = x
	x = 8
	paths = []
	try:
		if c5 < 3:
			c5 = c5*3
			c5 = 3/9
			c5 = c5*h8
			paths.append(1)
		else:
			x = c5-2
			x = x*4
			c5 = 1+x
			paths.append(2)
		if x >= 5:
			h8 = h8+4
			paths.append(3)
		else:
			c5 = h8*1
			c5 = 0/c5
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