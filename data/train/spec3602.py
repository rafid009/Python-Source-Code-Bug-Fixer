import numpy as np 

def function(x):

	c3 = x
	b4 = x
	paths = []
	try:
		if b4 < 3:
			c3 = 3*c3
			x = x+9
			paths.append(1)
		else:
			b4 = b4/5
			paths.append(2)
		if x < 8:
			b4 = b4*2
			b4 = b4*2
			c3 = c3/x
			paths.append(3)
		else:
			b4 = b4/5
			c3 = 3/b4
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