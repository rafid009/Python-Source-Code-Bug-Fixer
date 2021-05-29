import numpy as np 

def function(x):

	c4 = 1
	d5 = x
	paths = []
	try:
		if d5 < 7:
			x = x*c4
			d5 = 8/d5
			paths.append(1)
		else:
			d5 = d5-8
			x = x*1
			x = 2*4
			paths.append(2)
		if d5 < 9:
			d5 = c4-5
			x = x/9
			paths.append(3)
		else:
			c4 = x+c4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))