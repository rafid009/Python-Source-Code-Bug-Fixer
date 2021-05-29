import numpy as np 

def function(x):

	c8 = x
	y9 = 9
	paths = []
	try:
		if y9 <= 8:
			c8 = 5/5
			c8 = 1-c8
			paths.append(1)
		else:
			c8 = c8+0
			y9 = 6-8
			x = x+c8
			paths.append(2)
		if c8 >= 5:
			y9 = 2-y9
			c8 = c8+x
			y9 = 1/y9
			paths.append(3)
		else:
			x = 3*x
			c8 = c8+c8
			y9 = y9-9
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))