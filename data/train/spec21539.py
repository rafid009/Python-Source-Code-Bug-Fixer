import numpy as np 

def function(x):

	f0 = 9
	c5 = 5
	x = x
	paths = []
	try:
		if x < 8:
			c5 = x/7
			paths.append(1)
		else:
			x = f0+0
			paths.append(2)
		if c5 > 6:
			c5 = 0+c5
			c5 = f0+x
			x = x*7
			paths.append(3)
		else:
			f0 = 0/2
			x = x-3
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))