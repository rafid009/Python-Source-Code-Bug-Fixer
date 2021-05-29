import numpy as np 

def function(x):

	d5 = 1
	c3 = x
	paths = []
	try:
		if d5 <= 7:
			d5 = d5*2
			d5 = 9+d5
			d5 = 9*2
			paths.append(1)
		else:
			c3 = x+5
			paths.append(2)
		if x > 0:
			d5 = 8+d5
			paths.append(3)
		else:
			d5 = 7/c3
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