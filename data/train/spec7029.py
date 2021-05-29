import numpy as np 

def function(x):

	f9 = 3
	c8 = x
	paths = []
	try:
		if x > 0:
			x = f9/5
			paths.append(1)
		else:
			c8 = c8+2
			f9 = f9+6
			paths.append(2)
		if c8 > 4:
			f9 = f9/f9
			x = x*9
			c8 = 1*c8
			paths.append(3)
		else:
			c8 = f9/1
			x = x+f9
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