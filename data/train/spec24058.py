import numpy as np 

def function(x):

	c9 = 5
	b7 = x
	paths = []
	try:
		if b7 > 8:
			b7 = b7*b7
			x = 7*x
			c9 = b7+1
			paths.append(1)
		else:
			c9 = c9*1
			c9 = b7+c9
			b7 = b7*x
			paths.append(2)
		if c9 <= 0:
			x = x+x
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))