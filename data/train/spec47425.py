import numpy as np 

def function(x):

	w8 = 1
	c7 = x
	paths = []
	try:
		if c7 <= 9:
			x = 3+w8
			paths.append(1)
		else:
			x = x*x
			w8 = w8*c7
			paths.append(2)
		if w8 >= 2:
			w8 = 4*w8
			c7 = w8-0
			x = w8-3
			paths.append(3)
		else:
			w8 = x-c7
			x = 1/3
			w8 = 8*w8
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))