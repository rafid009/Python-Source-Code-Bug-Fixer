import numpy as np 

def function(x):

	d8 = 2
	c8 = 4
	x = 8
	paths = []
	try:
		if c8 >= 7:
			c8 = d8*c8
			paths.append(1)
		else:
			x = 6-d8
			d8 = x+7
			paths.append(2)
		if c8 < 9:
			c8 = 1-c8
			d8 = d8*3
			x = c8+d8
			paths.append(3)
		else:
			d8 = d8*8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		d8 = c8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))