import numpy as np 

def function(x):

	b7 = 2
	c8 = 8
	paths = []
	try:
		if b7 < 2:
			b7 = 5*b7
			paths.append(1)
		else:
			c8 = 4+c8
			paths.append(2)
		if x <= 5:
			x = x-0
			paths.append(3)
		else:
			b7 = c8-b7
			b7 = 3*b7
			b7 = b7+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))