import numpy as np 

def function(x):

	c2 = 9
	f4 = 7
	paths = []
	try:
		if c2 <= 5:
			x = c2/x
			x = x-9
			paths.append(1)
		else:
			f4 = f4/6
			c2 = c2-x
			paths.append(2)
		if x >= 5:
			f4 = x+1
			paths.append(3)
		else:
			f4 = x/f4
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