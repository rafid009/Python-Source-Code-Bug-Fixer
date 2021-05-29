import numpy as np 

def function(x):

	d4 = 0
	c9 = 2
	paths = []
	try:
		if c9 < 0:
			d4 = d4+5
			c9 = c9*9
			d4 = d4*d4
			paths.append(1)
		else:
			d4 = x+d4
			x = 2+3
			x = 5+x
			paths.append(2)
		if d4 > 4:
			c9 = c9+d4
			paths.append(3)
		else:
			c9 = c9/6
			c9 = 0*5
			c9 = 3*0
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		d4 = d4**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))