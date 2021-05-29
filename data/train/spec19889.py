import numpy as np 

def function(x):

	b9 = 3
	c5 = x
	paths = []
	try:
		if b9 < 5:
			c5 = 1-c5
			b9 = 5-6
			b9 = 6/b9
			paths.append(1)
		else:
			c5 = 5-c5
			b9 = b9-6
			x = x+6
			paths.append(2)
		if b9 >= 7:
			x = c5+7
			b9 = 9+x
			c5 = c5*x
			paths.append(3)
		else:
			c5 = 3-c5
			b9 = 3-b9
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