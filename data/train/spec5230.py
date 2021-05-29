import numpy as np 

def function(x):

	c8 = x
	w5 = x
	x = x
	paths = []
	try:
		if c8 > 0:
			w5 = w5*2
			x = 4-3
			w5 = w5+3
			paths.append(1)
		else:
			w5 = w5-x
			c8 = 1-c8
			c8 = 7-c8
			paths.append(2)
		if x > 1:
			c8 = c8+w5
			paths.append(3)
		else:
			c8 = c8+4
			x = x+1
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))