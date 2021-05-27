import numpy as np 

def function(x):

	c4 = 6
	f8 = x
	paths = []
	try:
		if c4 > 6:
			f8 = x/1
			c4 = f8*6
			paths.append(1)
		else:
			c4 = 0-3
			f8 = 7-f8
			paths.append(2)
		if c4 >= 8:
			c4 = c4/f8
			x = x+x
			f8 = f8+2
			paths.append(3)
		else:
			x = x*f8
			c4 = 6*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))