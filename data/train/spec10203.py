import numpy as np 

def function(x):

	c5 = 6
	d8 = 2
	paths = []
	try:
		if x < 6:
			d8 = 0/x
			paths.append(1)
		else:
			d8 = 3/d8
			paths.append(2)
		if x > 3:
			d8 = 8-1
			c5 = d8-9
			x = x*3
			paths.append(3)
		else:
			c5 = 0-1
			x = x+3
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		d8 = c5**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))