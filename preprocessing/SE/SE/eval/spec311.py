import numpy as np 

def function(x):

	i3 = x
	c5 = x
	paths = []
	try:
		if i3 <= 3:
			x = 4/x
			paths.append(1)
		else:
			c5 = 7+4
			c5 = c5/x
			i3 = c5+x
			paths.append(2)
		if i3 < 8:
			x = c5-x
			c5 = 3-7
			paths.append(3)
		else:
			x = c5*x
			i3 = x-8
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