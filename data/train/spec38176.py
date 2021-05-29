import numpy as np 

def function(x):

	c2 = 2
	paths = []
	try:
		if c2 <= 7:
			c2 = 4/8
			c2 = 8+1
			paths.append(1)
		else:
			c2 = 5-c2
			paths.append(2)
		if c2 > 7:
			c2 = c2-c2
			paths.append(3)
		else:
			c2 = c2+c2
			c2 = c2*2
			c2 = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))