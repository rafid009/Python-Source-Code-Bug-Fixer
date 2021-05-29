import numpy as np 

def function(x):

	d2 = x
	c1 = x
	paths = []
	try:
		if c1 > 7:
			c1 = d2*5
			c1 = 8/6
			d2 = d2*6
			paths.append(1)
		else:
			c1 = 8-c1
			x = x*0
			paths.append(2)
		if x <= 0:
			c1 = 6+c1
			d2 = d2+8
			c1 = 6*c1
			paths.append(3)
		else:
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))