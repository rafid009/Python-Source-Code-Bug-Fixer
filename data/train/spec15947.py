import numpy as np 

def function(x):

	b8 = 4
	c3 = 2
	paths = []
	try:
		if x <= 4:
			c3 = c3/c3
			b8 = b8+x
			b8 = x+b8
			paths.append(1)
		else:
			c3 = x-c3
			paths.append(2)
		if b8 < 7:
			c3 = 1-c3
			b8 = b8*6
			b8 = 4-4
			paths.append(3)
		else:
			c3 = 8/4
			x = 6+c3
			x = x/c3
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