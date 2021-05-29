import numpy as np 

def function(x):

	d8 = 6
	c1 = x
	x = 9
	paths = []
	try:
		if c1 <= 3:
			c1 = c1+8
			paths.append(1)
		else:
			d8 = d8*3
			paths.append(2)
		if c1 > 5:
			d8 = d8/3
			d8 = d8/d8
			paths.append(3)
		else:
			x = x-d8
			d8 = 4*d8
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		d8 = c1**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))