import numpy as np 

def function(x):

	j2 = x
	c5 = x
	paths = []
	try:
		if x > 8:
			x = 1+5
			j2 = c5-j2
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if c5 >= 8:
			c5 = j2*5
			paths.append(3)
		else:
			j2 = j2-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))