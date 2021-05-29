import numpy as np 

def function(x):

	c8 = x
	n3 = x
	paths = []
	try:
		if c8 > 5:
			c8 = 0*x
			n3 = 8*1
			c8 = x+c8
			paths.append(1)
		else:
			n3 = n3+c8
			c8 = 1-4
			c8 = c8/2
			paths.append(2)
		if c8 <= 0:
			c8 = 7/c8
			paths.append(3)
		else:
			c8 = c8+8
			c8 = 6*c8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		n3 = c8**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))