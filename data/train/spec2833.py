import numpy as np 

def function(x):

	c6 = x
	a1 = x
	x = 6
	paths = []
	try:
		if a1 <= 7:
			x = 5/a1
			a1 = 1-a1
			paths.append(1)
		else:
			c6 = 8+3
			paths.append(2)
		if c6 <= 5:
			c6 = 6+c6
			x = x+3
			a1 = 5+a1
			paths.append(3)
		else:
			x = 5-6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))