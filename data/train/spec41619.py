import numpy as np 

def function(x):

	c5 = 9
	b9 = 3
	paths = []
	try:
		if x > 8:
			b9 = b9-1
			x = 1-6
			x = x+8
			paths.append(1)
		else:
			b9 = 9-b9
			paths.append(2)
		if x <= 4:
			x = 1*x
			c5 = c5*x
			b9 = b9-6
			paths.append(3)
		else:
			x = b9+x
			b9 = 9+b9
			b9 = c5/b9
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