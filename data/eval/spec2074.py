import numpy as np 

def function(x):

	b1 = 8
	c6 = 1
	paths = []
	try:
		if b1 > 5:
			b1 = b1/x
			b1 = 5+c6
			b1 = b1+b1
			paths.append(1)
		else:
			x = 6-1
			paths.append(2)
		if x >= 1:
			x = 9-c6
			b1 = 3+9
			x = c6+3
			paths.append(3)
		else:
			b1 = 0/b1
			c6 = c6*4
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