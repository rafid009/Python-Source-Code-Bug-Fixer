import numpy as np 

def function(x):

	c5 = x
	o1 = 9
	paths = []
	try:
		if o1 <= 9:
			c5 = c5*8
			paths.append(1)
		else:
			x = 0*x
			paths.append(2)
		if o1 > 8:
			x = o1+x
			x = x+0
			paths.append(3)
		else:
			c5 = c5-x
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