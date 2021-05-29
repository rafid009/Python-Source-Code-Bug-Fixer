import numpy as np 

def function(x):

	c0 = x
	w8 = 2
	paths = []
	try:
		if w8 >= 2:
			c0 = c0/7
			x = x/2
			paths.append(1)
		else:
			w8 = 2-6
			w8 = 6*4
			x = w8*2
			paths.append(2)
		if x >= 6:
			c0 = 4+0
			paths.append(3)
		else:
			w8 = 6+w8
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