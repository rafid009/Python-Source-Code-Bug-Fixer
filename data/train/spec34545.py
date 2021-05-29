import numpy as np 

def function(x):

	d9 = x
	c9 = x
	paths = []
	try:
		if c9 <= 6:
			x = x+9
			paths.append(1)
		else:
			x = x+x
			x = x+5
			x = c9-4
			paths.append(2)
		if d9 >= 6:
			x = x/c9
			x = x-x
			d9 = 9*d9
			paths.append(3)
		else:
			d9 = x*c9
			c9 = 7*4
			x = d9+x
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		d9 = d9**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))