import numpy as np 

def function(x):

	c0 = x
	f5 = x
	x = x
	paths = []
	try:
		if x > 7:
			x = 9+f5
			c0 = 4/7
			paths.append(1)
		else:
			x = 0+x
			c0 = c0-1
			f5 = c0-f5
			paths.append(2)
		if x <= 7:
			c0 = x*5
			x = f5/5
			paths.append(3)
		else:
			f5 = f5*1
			x = 8-x
			f5 = 7-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))