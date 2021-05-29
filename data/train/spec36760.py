import numpy as np 

def function(x):

	d7 = 8
	c4 = 7
	x = 2
	paths = []
	try:
		if c4 > 5:
			d7 = c4+0
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x > 6:
			x = x+x
			paths.append(3)
		else:
			c4 = 5*c4
			c4 = d7-c4
			x = 4*3
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		d7 = c4**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))