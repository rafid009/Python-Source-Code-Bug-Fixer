import numpy as np 

def function(x):

	c2 = 4
	w8 = x
	x = x
	paths = []
	try:
		if x >= 1:
			x = x+c2
			w8 = 5*w8
			w8 = w8-7
			paths.append(1)
		else:
			c2 = c2-c2
			c2 = 7*1
			c2 = 3-3
			paths.append(2)
		if c2 <= 9:
			w8 = w8+8
			x = x-4
			paths.append(3)
		else:
			c2 = x-w8
			w8 = x-x
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