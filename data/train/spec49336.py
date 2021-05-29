import numpy as np 

def function(x):

	l8 = 8
	i2 = x
	paths = []
	try:
		if x <= 9:
			i2 = i2+l8
			l8 = l8*l8
			x = x/x
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if l8 < 9:
			l8 = l8*8
			x = 4-x
			paths.append(3)
		else:
			x = 3-l8
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