import numpy as np 

def function(x):

	c5 = 1
	f4 = 7
	paths = []
	try:
		if x > 6:
			x = x+3
			paths.append(1)
		else:
			x = x-2
			c5 = x-c5
			paths.append(2)
		if c5 > 4:
			x = x+0
			x = 4-x
			paths.append(3)
		else:
			f4 = 1-c5
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))