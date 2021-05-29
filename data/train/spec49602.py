import numpy as np 

def function(x):

	c1 = x
	d2 = x
	paths = []
	try:
		if x <= 8:
			x = x*1
			paths.append(1)
		else:
			d2 = 3+d2
			x = x+3
			x = x*7
			paths.append(2)
		if x >= 4:
			c1 = c1+6
			d2 = 6*d2
			paths.append(3)
		else:
			c1 = c1-7
			x = 9+x
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