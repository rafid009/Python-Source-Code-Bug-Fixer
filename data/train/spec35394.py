import numpy as np 

def function(x):

	d8 = x
	c6 = 7
	x = 2
	paths = []
	try:
		if d8 > 3:
			d8 = x*d8
			paths.append(1)
		else:
			x = x*x
			c6 = c6+c6
			x = c6-3
			paths.append(2)
		if d8 < 7:
			x = d8+x
			c6 = 4/8
			paths.append(3)
		else:
			x = 3*c6
			d8 = x-0
			d8 = 3-d8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))