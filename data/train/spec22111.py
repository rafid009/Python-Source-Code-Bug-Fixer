import numpy as np 

def function(x):

	c8 = x
	f4 = 8
	paths = []
	try:
		if c8 <= 5:
			f4 = 5*3
			x = 3/x
			f4 = f4-f4
			paths.append(1)
		else:
			x = 8/6
			x = 2+x
			x = 2*x
			paths.append(2)
		if c8 <= 0:
			x = 9-8
			f4 = f4-2
			c8 = c8/9
			paths.append(3)
		else:
			x = x*9
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