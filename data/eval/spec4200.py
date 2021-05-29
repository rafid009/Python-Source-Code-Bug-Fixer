import numpy as np 

def function(x):

	c3 = 9
	b1 = x
	paths = []
	try:
		if c3 >= 3:
			b1 = x+b1
			c3 = c3/7
			x = x-2
			paths.append(1)
		else:
			x = 1+x
			b1 = c3/b1
			paths.append(2)
		if c3 < 8:
			c3 = b1+x
			c3 = 0/6
			c3 = x+3
			paths.append(3)
		else:
			x = b1/5
			x = x-4
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