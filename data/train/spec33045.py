import numpy as np 

def function(x):

	c2 = x
	b1 = x
	paths = []
	try:
		if b1 >= 3:
			b1 = 6+b1
			c2 = x-x
			x = x-6
			paths.append(1)
		else:
			x = x-6
			c2 = 9/c2
			x = 3*c2
			paths.append(2)
		if b1 <= 7:
			b1 = 7*b1
			paths.append(3)
		else:
			x = 0-0
			x = 4+x
			c2 = 0*b1
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		c2 = c2**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))