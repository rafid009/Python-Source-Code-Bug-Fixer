import numpy as np 

def function(x):

	c3 = 7
	d4 = x
	x = x
	paths = []
	try:
		if x >= 3:
			x = x*3
			d4 = d4*0
			d4 = d4-5
			paths.append(1)
		else:
			c3 = c3+0
			d4 = c3/d4
			c3 = c3/d4
			paths.append(2)
		if x <= 9:
			d4 = d4-4
			paths.append(3)
		else:
			x = x*4
			c3 = 0/c3
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))