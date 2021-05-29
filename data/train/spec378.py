import numpy as np 

def function(x):

	v2 = x
	c8 = 5
	paths = []
	try:
		if x < 6:
			v2 = 5*v2
			c8 = c8*x
			paths.append(1)
		else:
			c8 = 2-6
			c8 = v2/c8
			paths.append(2)
		if x > 8:
			v2 = v2+x
			v2 = v2-1
			paths.append(3)
		else:
			v2 = x/4
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		c8 = v2**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))