import numpy as np 

def function(x):

	b4 = x
	c5 = 5
	paths = []
	try:
		if b4 < 6:
			c5 = 9/9
			paths.append(1)
		else:
			b4 = b4*c5
			c5 = c5+2
			b4 = x/b4
			paths.append(2)
		if b4 > 6:
			c5 = c5*4
			c5 = 5+c5
			x = 8+2
			paths.append(3)
		else:
			b4 = b4/7
			c5 = b4/c5
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))