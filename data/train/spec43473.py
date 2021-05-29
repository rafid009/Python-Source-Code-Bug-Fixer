import numpy as np 

def function(x):

	c3 = x
	v9 = x
	paths = []
	try:
		if c3 < 8:
			c3 = 8+c3
			v9 = 6-v9
			paths.append(1)
		else:
			x = x*1
			c3 = 5*c3
			c3 = c3/v9
			paths.append(2)
		if x <= 4:
			x = v9+v9
			x = c3+c3
			paths.append(3)
		else:
			c3 = c3+2
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		c3 = v9**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))