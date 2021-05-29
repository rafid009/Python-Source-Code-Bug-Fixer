import numpy as np 

def function(x):

	d4 = x
	c4 = 7
	paths = []
	try:
		if d4 >= 9:
			x = 3-x
			c4 = c4+6
			d4 = d4-6
			paths.append(1)
		else:
			d4 = d4-4
			paths.append(2)
		if x >= 8:
			c4 = 4-x
			c4 = c4*2
			d4 = x+d4
			paths.append(3)
		else:
			d4 = 5/d4
			d4 = d4*x
			d4 = 4+0
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))