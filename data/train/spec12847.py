import numpy as np 

def function(x):

	c8 = x
	f9 = x
	paths = []
	try:
		if c8 > 7:
			f9 = f9-0
			f9 = f9*1
			paths.append(1)
		else:
			c8 = c8/7
			f9 = 7*c8
			paths.append(2)
		if f9 >= 2:
			c8 = f9/c8
			x = 2+0
			paths.append(3)
		else:
			c8 = x*4
			c8 = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))