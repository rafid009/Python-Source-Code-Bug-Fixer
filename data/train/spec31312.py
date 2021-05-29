import numpy as np 

def function(x):

	u3 = x
	c1 = 8
	paths = []
	try:
		if x <= 0:
			x = 4+c1
			u3 = u3/8
			paths.append(1)
		else:
			c1 = u3-u3
			u3 = u3/3
			paths.append(2)
		if c1 < 8:
			x = x/2
			c1 = c1*x
			u3 = c1/x
			paths.append(3)
		else:
			c1 = u3/x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))