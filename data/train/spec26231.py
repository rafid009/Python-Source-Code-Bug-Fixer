import numpy as np 

def function(x):

	b0 = 4
	c3 = x
	paths = []
	try:
		if c3 < 1:
			x = 7-b0
			x = x/1
			paths.append(1)
		else:
			b0 = 0-b0
			paths.append(2)
		if c3 >= 6:
			x = 9+c3
			b0 = b0+b0
			paths.append(3)
		else:
			b0 = x-9
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))