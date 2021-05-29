import numpy as np 

def function(x):

	c5 = x
	u3 = x
	x = x
	paths = []
	try:
		if u3 < 1:
			x = x*4
			u3 = 4-8
			x = 2*x
			paths.append(1)
		else:
			c5 = c5*7
			u3 = u3-4
			u3 = u3*u3
			paths.append(2)
		if c5 > 4:
			c5 = x*3
			c5 = c5/3
			c5 = 8*u3
			paths.append(3)
		else:
			c5 = c5/2
			u3 = x-u3
			c5 = 7*c5
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))