import numpy as np 

def function(x):

	o0 = 8
	c8 = x
	paths = []
	try:
		if o0 >= 5:
			o0 = x*2
			c8 = c8+8
			paths.append(1)
		else:
			x = 3+x
			x = 5+c8
			paths.append(2)
		if x >= 7:
			x = x+7
			c8 = 3-c8
			paths.append(3)
		else:
			c8 = 6*9
			o0 = 4/x
			c8 = 1+c8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		c8 = c8**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))