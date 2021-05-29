import numpy as np 

def function(x):

	b8 = 1
	c5 = 8
	paths = []
	try:
		if x < 4:
			x = 4+x
			b8 = x+b8
			paths.append(1)
		else:
			b8 = x-2
			b8 = b8/3
			x = 3-8
			paths.append(2)
		if x <= 8:
			b8 = 0*4
			x = x*4
			paths.append(3)
		else:
			c5 = b8-3
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