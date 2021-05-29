import numpy as np 

def function(x):

	b3 = x
	c2 = 3
	paths = []
	try:
		if c2 > 7:
			x = 0*x
			paths.append(1)
		else:
			c2 = c2+5
			c2 = 9*3
			paths.append(2)
		if b3 > 6:
			c2 = c2*c2
			b3 = b3+x
			x = x*3
			paths.append(3)
		else:
			b3 = b3+1
			c2 = 3+0
			b3 = 6+c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))