import numpy as np 

def function(x):

	v4 = x
	c7 = x
	paths = []
	try:
		if v4 <= 6:
			c7 = 7*c7
			paths.append(1)
		else:
			c7 = v4/9
			paths.append(2)
		if c7 < 4:
			x = 4+x
			c7 = c7+3
			x = x*0
			paths.append(3)
		else:
			v4 = v4-6
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		c7 = v4**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))