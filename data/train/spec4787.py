import numpy as np 

def function(x):

	c4 = 1
	v3 = 1
	paths = []
	try:
		if v3 > 5:
			c4 = c4/x
			c4 = c4*5
			v3 = x-2
			paths.append(1)
		else:
			c4 = x/9
			paths.append(2)
		if x < 6:
			v3 = 8*c4
			paths.append(3)
		else:
			c4 = c4-0
			v3 = v3*9
			x = x*5
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		c4 = v3**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))