import numpy as np 

def function(x):

	c2 = 5
	f5 = x
	paths = []
	try:
		if f5 <= 7:
			c2 = x*9
			x = 7-8
			c2 = x/5
			paths.append(1)
		else:
			f5 = f5*3
			f5 = 5*4
			paths.append(2)
		if x >= 3:
			f5 = f5-5
			paths.append(3)
		else:
			c2 = f5/8
			c2 = 3/c2
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