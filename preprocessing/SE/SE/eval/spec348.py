import numpy as np 

def function(x):

	v1 = 6
	c4 = x
	paths = []
	try:
		if v1 <= 3:
			x = c4*x
			paths.append(1)
		else:
			x = x*9
			x = c4+x
			v1 = c4*1
			paths.append(2)
		if c4 > 7:
			x = x*4
			c4 = v1/c4
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		c4 = v1**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))