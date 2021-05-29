import numpy as np 

def function(x):

	c2 = x
	d8 = 9
	paths = []
	try:
		if d8 >= 9:
			c2 = c2/9
			c2 = 7+0
			paths.append(1)
		else:
			x = 3+x
			d8 = d8-9
			d8 = c2-7
			paths.append(2)
		if c2 <= 9:
			x = x*8
			paths.append(3)
		else:
			c2 = x/x
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