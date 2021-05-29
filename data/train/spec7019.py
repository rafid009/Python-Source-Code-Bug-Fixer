import numpy as np 

def function(x):

	b5 = x
	c8 = 1
	paths = []
	try:
		if x <= 7:
			c8 = c8/x
			paths.append(1)
		else:
			x = c8*4
			paths.append(2)
		if x > 3:
			b5 = b5*c8
			b5 = b5/b5
			x = x/2
			paths.append(3)
		else:
			b5 = 9+b5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))